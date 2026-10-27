#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Red Team v5.1.0 Regression Suite for DESIGN:OS Vietnamese.

Covers all 8 Red Team audit findings and 5 architectural upgrades:
  1. Unicode NFD normalization before linguistic/domain regex evaluation
  2. DIACRITIC_PHRASES 'thanh cong' detection without false positives on ', thành công'
  3. NUM003 thousand-grouping (5.000 tỷ, 20.000 m²) vs decimal period (5.25%)
  4. NUM004 unspaced 50m2/100m3 detection + hardware 'Ổ cứng M2 SSD' exemption
  5. LAW001 ordinal exemptions ('Bước số 1', 'Trang số 1') & span deduplication
  6. PRO002 compound exemptions ('người bạn', 'quý công ty', 'quý này')
  7. ICU001/ICU002 fenced code block masking & JSON key masking
  8. Inline suppression ('vncopy-disable', 'vlc-disable', bare '*-disable-line')
  9. Multi-domain '--domain finance,legal' & '--domain all' + stdin ('-')
 10. Domain statutory hardening (FIN008 HTML <ul>, EDU005 tín dụng, REA002 đợt 1,
     LEG001 contract context, LEG005 superseded laws, ECOM005 logistics calques,
     and negation/meta-discourse guard)
 11. check_i18n_parity.py JSON arrays, '{count, number}', Apple .xcstrings,
     Android strings.xml, and placeholder length discounting
 12. check_font_coverage.py --json and non-Latin symbol filtering
 13. Complete local reference files across all 16 skills
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys
import tempfile
import unicodedata
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
VALIDATE_COPY = ROOT / "shared" / "scripts" / "validate_copy.py"
CHECK_PARITY = ROOT / "shared" / "scripts" / "check_i18n_parity.py"
CHECK_FONT = ROOT / "shared" / "scripts" / "check_font_coverage.py"


def run_cmd(*args: object, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *map(str, args)],
        input=input_text,
        capture_output=True,
        text=True,
        cwd=ROOT,
    )


class RedTeamEngineHardeningTests(unittest.TestCase):
    """Tests core engine fixes in shared/scripts/validate_copy.py."""

    def test_nfd_input_does_not_bypass_linguistic_or_statutory_rules(self) -> None:
        nfd_sample = unicodedata.normalize(
            "NFD",
            "Như một quản trị viên, tôi muốn bạn và quý khách dùng nền tảng số 1 Việt Nam.\n",
        )
        r = run_cmd(VALIDATE_COPY, "-", "--json", input_text=nfd_sample)
        self.assertEqual(r.returncode, 1)
        payload = json.loads(r.stdout)
        rules = {f["rule"] for f in payload["findings"]}
        self.assertIn("NFC001", rules)
        self.assertIn("SYN001", rules)
        self.assertIn("PRO001", rules)
        self.assertIn("LAW001", rules)

    def test_dia001_detects_unaccented_thanh_cong_without_false_positive(self) -> None:
        r_good = run_cmd(
            VALIDATE_COPY,
            "-",
            "--json",
            input_text="Giao dịch đã hoàn tất, thành công và an toàn.\n",
        )
        self.assertEqual(r_good.returncode, 0, r_good.stdout)

        r_bad = run_cmd(
            VALIDATE_COPY,
            "-",
            "--json",
            input_text="Giao dich thanh cong tren he thong.\n",
        )
        payload = json.loads(r_bad.stdout)
        rules = {f["rule"] for f in payload["findings"]}
        self.assertIn("DIA001", rules)

    def test_num003_allows_vietnamese_thousands_grouping_and_flags_decimals(self) -> None:
        r_good = run_cmd(
            VALIDATE_COPY,
            "-",
            "--json",
            input_text="Quy mô dự án đạt 5.000 tỷ đồng trên diện tích 20.000 m² với 1.500 điểm giao dịch.\n",
        )
        payload_good = json.loads(r_good.stdout)
        rules_good = {f["rule"] for f in payload_good["findings"]}
        self.assertNotIn("NUM003", rules_good)

        r_bad = run_cmd(
            VALIDATE_COPY,
            "-",
            "--json",
            input_text="Lãi suất ưu đãi chỉ 6.5% mỗi năm cho khoản vay 1.25 tỷ đồng.\n",
        )
        payload_bad = json.loads(r_bad.stdout)
        rules_bad = {f["rule"] for f in payload_bad["findings"]}
        self.assertIn("NUM003", rules_bad)

    def test_num004_catches_unspaced_50m2_and_exempts_hardware_m2_ssd(self) -> None:
        r_bad = run_cmd(
            VALIDATE_COPY,
            "-",
            "--json",
            input_text="Căn hộ diện tích 50m2 và bể bơi 120m3.\n",
        )
        payload_bad = json.loads(r_bad.stdout)
        num004 = [f for f in payload_bad["findings"] if f["rule"] == "NUM004"]
        self.assertEqual(len(num004), 2)

        r_good = run_cmd(
            VALIDATE_COPY,
            "-",
            "--json",
            input_text="Máy trạm trang bị chip Apple M2 và ổ cứng M2 SSD 1TB tốc độ cao.\n",
        )
        payload_good = json.loads(r_good.stdout)
        rules_good = {f["rule"] for f in payload_good["findings"]}
        self.assertNotIn("NUM004", rules_good)

    def test_law001_exempts_ordinals_and_deduplicates_superlative_spans(self) -> None:
        r_good = run_cmd(
            VALIDATE_COPY,
            "-",
            "--json",
            input_text=" Thực hiện bước số 1 tại trang số 1, phụ lục số 1 để có trải nghiệm tốt nhất.\n",
        )
        payload_good = json.loads(r_good.stdout)
        rules_good = {f["rule"] for f in payload_good["findings"]}
        self.assertNotIn("LAW001", rules_good)

        r_bad = run_cmd(
            VALIDATE_COPY,
            "-",
            "--json",
            input_text="Sản phẩm tốt nhất Việt Nam trên thị trường.\n",
        )
        payload_bad = json.loads(r_bad.stdout)
        law001 = [f for f in payload_bad["findings"] if f["rule"] == "LAW001"]
        self.assertEqual(len(law001), 1)

    def test_pro002_exempts_nguoi_ban_and_quy_cong_ty(self) -> None:
        r_good = run_cmd(
            VALIDATE_COPY,
            "-",
            "--json",
            input_text="Quý khách có thể giới thiệu những người bạn thân thiết trong quý này.\n",
        )
        payload_good = json.loads(r_good.stdout)
        rules_good = {f["rule"] for f in payload_good["findings"]}
        self.assertNotIn("PRO002", rules_good)

    def test_fenced_code_block_masks_icu_and_json_masks_keys(self) -> None:
        md_text = (
            "Hướng dẫn cấu hình ICU MessageFormat:\n\n"
            "```json\n"
            "{\n"
            '  "files": "{count, plural, one {# file} other {# files}}",\n'
            '  "translated_var": "{so_luong}"\n'
            "}\n"
            "```\n"
        )
        r_md = run_cmd(VALIDATE_COPY, "-", "--json", input_text=md_text)
        payload_md = json.loads(r_md.stdout)
        rules_md = {f["rule"] for f in payload_md["findings"]}
        self.assertNotIn("ICU001", rules_md)
        self.assertNotIn("ICU002", rules_md)

        with tempfile.NamedTemporaryFile("w", suffix=".json", encoding="utf-8", delete=False) as tf:
            json.dump({"m2": "Diện tích 50 m²", "thanh_cong": "Giao dịch thành công"}, tf, ensure_ascii=False)
            json_path = pathlib.Path(tf.name)
        try:
            r_json = run_cmd(VALIDATE_COPY, json_path, "--json")
            payload_json = json.loads(r_json.stdout)
            self.assertEqual(payload_json["findings"], [])
        finally:
            json_path.unlink(missing_ok=True)

    def test_vncopy_disable_and_disable_line_directives(self) -> None:
        doc = (
            "<!-- vncopy-disable: LAW001 -->\n"
            "Giải pháp số 1 Việt Nam.\n"
            "Được thiết kế bởi chuyên gia. <!-- vncopy-disable-line -->\n"
        )
        r = run_cmd(VALIDATE_COPY, "-", "--json", input_text=doc)
        payload = json.loads(r.stdout)
        self.assertEqual(payload["findings"], [])

    def test_multi_domain_composition_and_domain_all(self) -> None:
        sample = (
            "Cam kết lợi nhuận 18%/năm. Hợp đồng phạt vi phạm hợp đồng 15% tổng giá trị.\n"
        )
        r = run_cmd(VALIDATE_COPY, "-", "--domain", "finance,legal", "--json", input_text=sample)
        payload = json.loads(r.stdout)
        rules = {f["rule"] for f in payload["findings"]}
        self.assertIn("FIN001", rules)
        self.assertIn("LEG001", rules)

        r_all = run_cmd(VALIDATE_COPY, "--domain", "all", "--list-rules")
        self.assertEqual(r_all.returncode, 0)
        for prefix in ("UX001", "FIN001", "LEG001", "REA001", "ECOM001", "GOV001", "INS001", "SEC001", "MEDJ001"):
            self.assertIn(prefix, r_all.stdout)


class RedTeamDomainStatutoryTests(unittest.TestCase):
    """Tests domain rule precision and statutory updates across skills/*/scripts/rules_*.py."""

    def test_fin008_ignores_html_ul_and_flags_ulip_without_warning(self) -> None:
        html_doc = "<ul><li>Biểu phí dịch vụ ngân hàng số 0 đồng.</li></ul>\n"
        r_good = run_cmd(VALIDATE_COPY, "-", "--domain", "finance", "--json", input_text=html_doc)
        rules_good = {f["rule"] for f in json.loads(r_good.stdout)["findings"]}
        self.assertNotIn("FIN008", rules_good)

        ulip_doc = "Sản phẩm bảo hiểm liên kết chung mang lại sự bảo vệ linh hoạt.\n"
        r_bad = run_cmd(VALIDATE_COPY, "-", "--domain", "finance", "--json", input_text=ulip_doc)
        rules_bad = {f["rule"] for f in json.loads(r_bad.stdout)["findings"]}
        self.assertIn("FIN008", rules_bad)

    def test_edu005_ignores_tin_dung_sinh_vien(self) -> None:
        doc = "Ngân hàng Chính sách Xã hội triển khai gói tín dụng sinh viên lãi suất ưu đãi.\n"
        r = run_cmd(VALIDATE_COPY, "-", "--domain", "edu", "--json", input_text=doc)
        rules = {f["rule"] for f in json.loads(r.stdout)["findings"]}
        self.assertNotIn("EDU005", rules)

    def test_rea002_ignores_revenue_dot_1_and_flags_first_installment_over_30_percent(self) -> None:
        good_doc = "Doanh thu đợt 1 đạt 80% kế hoạch kinh doanh năm.\n"
        r_good = run_cmd(VALIDATE_COPY, "-", "--domain", "realestate", "--json", input_text=good_doc)
        rules_good = {f["rule"] for f in json.loads(r_good.stdout)["findings"]}
        self.assertNotIn("REA002", rules_good)

        bad_doc = "Khách hàng thanh toán đợt 1 là 50% giá trị hợp đồng mua bán căn hộ.\n"
        r_bad = run_cmd(VALIDATE_COPY, "-", "--domain", "realestate", "--json", input_text=bad_doc)
        rules_bad = {f["rule"] for f in json.loads(r_bad.stdout)["findings"]}
        self.assertIn("REA002", rules_bad)

    def test_leg001_requires_contract_context_and_leg005_flags_2005_2009_laws(self) -> None:
        good_doc = "Tỷ lệ tăng trưởng doanh thu đạt 15% trong năm tài chính.\n"
        r_good = run_cmd(VALIDATE_COPY, "-", "--domain", "legal", "--json", input_text=good_doc)
        rules_good = {f["rule"] for f in json.loads(r_good.stdout)["findings"]}
        self.assertNotIn("LEG001", rules_good)

        bad_doc = "Căn cứ Luật Giao dịch điện tử 2005 và Luật Viễn thông 2009, mức phạt cọc 15%.\n"
        r_bad = run_cmd(VALIDATE_COPY, "-", "--domain", "legal", "--json", input_text=bad_doc)
        rules_bad = {f["rule"] for f in json.loads(r_bad.stdout)["findings"]}
        self.assertIn("LEG005", rules_bad)

    def test_ecom005_flags_untranslated_logistics_calques(self) -> None:
        bad_doc = "Đơn hàng đang out for delivery, tài xế sẽ gửi pod trước 17:00.\n"
        r_bad = run_cmd(VALIDATE_COPY, "-", "--domain", "ecommerce", "--json", input_text=bad_doc)
        rules_bad = {f["rule"] for f in json.loads(r_bad.stdout)["findings"]}
        self.assertIn("ECOM005", rules_bad)

    def test_negation_and_meta_discourse_guard_prevents_false_positives(self) -> None:
        hr_meta = "Lưu ý pháp lý: Bộ luật Lao động 2019 đã bãi bỏ hợp đồng mùa vụ dưới 12 tháng.\n"
        r_hr = run_cmd(VALIDATE_COPY, "-", "--domain", "hr", "--json", input_text=hr_meta)
        rules_hr = {f["rule"] for f in json.loads(r_hr.stdout)["findings"]}
        self.assertNotIn("HR002", rules_hr)

        med_meta = "Quy định tuân thủ: Không được quảng cáo thực phẩm bảo vệ sức khỏe là thần dược trị bách bệnh.\n"
        r_med = run_cmd(VALIDATE_COPY, "-", "--domain", "healthcare", "--json", input_text=med_meta)
        rules_med = {f["rule"] for f in json.loads(r_med.stdout)["findings"]}
        self.assertNotIn("MED001", rules_med)


class RedTeamMultiPlatformCatalogAndFontTests(unittest.TestCase):
    """Tests check_i18n_parity.py and check_font_coverage.py multi-platform features."""

    def test_i18n_parity_json_arrays_and_icu_formatted_placeholders(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            en_path = pathlib.Path(tmp) / "en.json"
            vi_path = pathlib.Path(tmp) / "vi.json"
            en_path.write_text(
                json.dumps(
                    {
                        "summary": "Found {count} items",
                        "steps": ["Step {step_num}", "Missing {extra_var}"],
                        "cta.button": "Save {user_organization_display_name}",
                    }
                ),
                encoding="utf-8",
            )
            vi_path.write_text(
                json.dumps(
                    {
                        "summary": "Tìm thấy {count, number} mục",
                        "steps": ["Bước {step_num}", "Hoàn tất"],
                        "cta.button": "Lưu {user_organization_display_name}",
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            r = run_cmd(CHECK_PARITY, en_path, vi_path, "--json")
            payload = json.loads(r.stdout)
            by_key = {(f["key"], f["rule"]) for f in payload["findings"]}
            # {count} vs {count, number} is valid -> no I18N003 on summary
            self.assertNotIn(("summary", "I18N003"), by_key)
            # Array item steps[1] missing {extra_var} -> flagged!
            self.assertIn(("steps[1]", "I18N003"), by_key)
            # Long placeholder name discounted -> no UX001 on cta.button
            self.assertNotIn(("cta.button", "UX001"), by_key)

    def test_i18n_parity_apple_xcstrings_and_android_xml(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            xc_path = pathlib.Path(tmp) / "Localizable.xcstrings"
            xc_path.write_text(
                json.dumps(
                    {
                        "sourceLanguage": "en",
                        "strings": {
                            "greeting": {
                                "localizations": {
                                    "en": {"stringUnit": {"state": "translated", "value": "Hello %1$@"}},
                                    "vi": {"stringUnit": {"state": "translated", "value": "Xin chào %1$@"}},
                                }
                            },
                            "missing_vi": {
                                "localizations": {
                                    "en": {"stringUnit": {"state": "translated", "value": "Continue"}},
                                }
                            },
                        },
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            r_xc = run_cmd(CHECK_PARITY, xc_path, "--json")
            payload_xc = json.loads(r_xc.stdout)
            rules_xc = {(f["key"], f["rule"]) for f in payload_xc["findings"]}
            self.assertIn(("missing_vi", "I18N001"), rules_xc)
            self.assertNotIn(("greeting", "I18N003"), rules_xc)

            en_xml = pathlib.Path(tmp) / "strings-en.xml"
            vi_xml = pathlib.Path(tmp) / "strings-vi.xml"
            en_xml.write_text(
                '<resources><string name="welcome">Hello %1$s</string></resources>',
                encoding="utf-8",
            )
            vi_xml.write_text(
                '<resources><string name="welcome">Xin chào %1$s</string></resources>',
                encoding="utf-8",
            )
            r_xml = run_cmd(CHECK_PARITY, en_xml, vi_xml, "--json")
            self.assertEqual(r_xml.returncode, 0, r_xml.stdout)

    def test_font_coverage_json_and_symbol_filtering(self) -> None:
        with tempfile.NamedTemporaryFile("w", suffix=".md", encoding="utf-8", delete=False) as tf:
            tf.write("Chuyển khoản nhanh 24/7 → Nhận tiền tức thì • Hoàn toàn miễn phí ✅\n")
            md_path = pathlib.Path(tf.name)
        try:
            r_default = run_cmd(CHECK_FONT, md_path, "--json")
            self.assertEqual(r_default.returncode, 0, r_default.stdout)
            payload = json.loads(r_default.stdout)
            self.assertEqual(payload["uncovered_count"], 0)

            r_strict = run_cmd(CHECK_FONT, md_path, "--strict-symbols", "--json")
            self.assertEqual(r_strict.returncode, 1)
            payload_strict = json.loads(r_strict.stdout)
            self.assertGreaterEqual(payload_strict["uncovered_count"], 2)
        finally:
            md_path.unlink(missing_ok=True)

    def test_all_16_skills_have_complete_local_references(self) -> None:
        skills_dir = ROOT / "skills"
        for skill_path in sorted(skills_dir.iterdir()):
            if not skill_path.is_dir():
                continue
            for ref_name in ("glossary.md", "banned-phrases.md", "qa-checklist.md"):
                ref_file = skill_path / "references" / ref_name
                self.assertTrue(ref_file.is_file(), f"Missing {ref_file.relative_to(ROOT)}")
                self.assertGreater(ref_file.stat().st_size, 500, f"Empty/stub {ref_file.relative_to(ROOT)}")


if __name__ == "__main__":
    unittest.main()
