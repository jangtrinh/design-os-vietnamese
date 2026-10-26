# -*- coding: utf-8 -*-
"""Rules for Vietnamese healthcare, medical, hospital, EMR, and pharmaceutical copy.

Loaded automatically by validate_copy.py because the filename starts with `rules_`.
Pure Python standard library only.

This module enforces statutory and regulatory compliance across Vietnamese medical
and pharmaceutical communications:
- Luật Khám bệnh, chữa bệnh số 15/2023/QH15 (hiệu lực 01/01/2024: bãi bỏ 'Chứng chỉ hành nghề',
  thay thế bằng 'Giấy phép hành nghề khám bệnh, chữa bệnh', quy định quyền người bệnh và EMR)
- Thông tư 32/2023/TT-BYT (Quy định chi tiết thi hành Luật KCB 2023, hồ sơ bệnh án điện tử EMR,
  tóm tắt bệnh án và giấy ra viện)
- Nghị định 15/2018/NĐ-CP & Thông tư 05/2018/TT-BYT (Quy định chi tiết thi hành Luật An toàn
  thực phẩm, câu khuyến cáo bắt buộc cho Thực phẩm bảo vệ sức khỏe TPCN, cấm dùng thư cảm ơn,
  cấm bác sĩ/nhân viên y tế quảng cáo TPCN)
- Thông tư 52/2017/TT-BYT, TT 18/2018/TT-BYT & Thông tư 27/2021/TT-BYT (Kê đơn thuốc ngoại trú,
  đơn thuốc điện tử Quốc gia, cấm hướng dẫn liều lượng mơ hồ)
- Luật Dược 2016 & Luật sửa đổi số 44/2024/QH15 (Quy chế thông tin thuốc và cảnh báo dược)
- Luật Quảng cáo 2012 số 16/2012/QH13 (Nghiêm cấm cam kết khỏi bệnh 100%, thổi phồng 'thần dược')

Rules:
- MED001 (ERROR): TPCN ad missing mandatory statutory disclaimer
- MED002 (ERROR): Prohibited therapeutic/curative claims ('chữa khỏi hoàn toàn 100%', 'thần dược')
- MED003 (WARNING): Obsolete licensing terminology ('Chứng chỉ hành nghề y/KCB')
- MED004 (ERROR): Vague dosage or missing route/timing/warning instructions in prescription
- MED005 (ERROR): Prohibited patient testimonial / doctor endorsement for TPCN / clinic
- MED006 (WARNING): Stigmatizing, alarmist, or patient-blaming language in healthcare comms
- MED007 (ERROR): Discharge summary missing red-flag emergency return instructions
"""
from __future__ import annotations

import re
from typing import Iterator, Tuple

ERROR = "error"
WARN = "warning"

RULE_DOCS = {
    "MED001": "mandatory statutory disclaimer missing in TPCN advertising ('Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh' — Nghị định 15/2018/NĐ-CP Điều 27)",
    "MED002": "prohibited therapeutic or curative claims for supplements or medical services ('chữa khỏi hoàn toàn 100%', 'điều trị dứt điểm vĩnh viễn', 'thần dược trị bách bệnh' — NĐ 15/2018; Luật Dược; Luật KCB 2023)",
    "MED003": "obsolete licensing terminology ('Chứng chỉ hành nghề y/KCB'); replaced by 'Giấy phép hành nghề' under Luật Khám bệnh, chữa bệnh 2023 số 15/2023/QH15",
    "MED004": "vague dosage instructions or missing explicit route/timing/dosage units/warning signs in prescription (Thông tư 52/2017/TT-BYT & TT 27/2021/TT-BYT)",
    "MED005": "prohibited patient testimonial or doctor endorsement tactics in healthcare/TPCN copy (Nghị định 15/2018/NĐ-CP; Luật Quảng cáo 2012)",
    "MED006": "stigmatizing, alarmist, or patient-blaming language in clinical or patient communications",
    "MED007": "discharge summary missing red-flag emergency return instructions ('dấu hiệu cần tái khám ngay' / cấp cứu — Thông tư 32/2023/TT-BYT)",
}

DOCTYPES = {
    "tpcn-ad": "Quảng cáo / Mô tả Thực phẩm bảo vệ sức khỏe (TPCN — Nghị định 15/2018/NĐ-CP & Thông tư 05/2018/TT-BYT)",
    "prescription": "Đơn thuốc ngoại trú / Hướng dẫn dùng thuốc (Thông tư 52/2017/TT-BYT & TT 27/2021/TT-BYT đơn thuốc điện tử)",
    "discharge-summary": "Giấy ra viện / Hướng dẫn theo dõi sau xuất viện (Thông tư 32/2023/TT-BYT)",
    "emr-note": "Hồ sơ bệnh án điện tử EMR / Phiếu trả kết quả cận lâm sàng (Thông tư 32/2023/TT-BYT & Luật Khám bệnh, chữa bệnh 2023)",
    "clinic-landing": "Trang giới thiệu bệnh viện, phòng khám chuyên khoa, dịch vụ tầm soát",
}

# MED001: Statutory TPCN disclaimer under NĐ 15/2018/NĐ-CP Điều 27
TPCN_DISCLAIMER_RE = re.compile(
    r"thực\s+phẩm\s+này\s+không\s+phải\s+là\s+thuốc\s+(?:và\s+)?không\s+có\s+tác\s+dụng\s+thay\s+thế\s+thuốc\s+chữa\s+bệnh",
    re.IGNORECASE,
)

# MED002: Prohibited therapeutic or absolute curative promises
CURATIVE_CLAIMS_PATTERNS = (
    r"chữa\s+khỏi\s+hoàn\s+toàn\s*100\s*%",
    r"điều\s+trị\s+dứt\s+điểm\s+vĩnh\s+viễn",
    r"cam\s+kết\s+khỏi\s+(?:bệnh\s+)?100\s*%",
    r"thần\s+dược\s+trị\s+bách\s+bệnh",
    r"thay\s+thế\s+hoàn\s+toàn\s+thuốc\s+đặc\s+trị",
    r"trị\s+dứt\s+điểm\s+100\s*%",
    r"khỏi\s+bệnh\s+hoàn\s+toàn\s*100\s*%",
    r"cam\s+kết\s+chữa\s+khỏi\s*100\s*%",
    r"chữa\s+dứt\s+điểm\s*100\s*%",
    r"thần\s+dược\s+(?:trị|chữa)\s+bệnh",
    r"chữa\s+khỏi\s+hoàn\s+toàn\s+ung\s+thư",
    r"thần\s+dược\s+phòng\s+the",
    r"chữa\s+bách\s+bệnh",
)
CURATIVE_COMPILED = [re.compile(p, re.IGNORECASE) for p in CURATIVE_CLAIMS_PATTERNS]

# MED003: Obsolete licensing terminology under Luật KCB 2023
OBSOLETE_LICENSE_RE = re.compile(
    r"(?<!\w)chứng\s+chỉ\s+hành\s+nghề\s+(?:khám\s+bệnh,\s*chữa\s+bệnh|khám\s+bệnh\s+chữa\s+bệnh|khám\s+chữa\s+bệnh|y(?:\s+khoa|\s+tế)?|y\b)(?!\w)",
    re.IGNORECASE,
)

# MED004: Vague dosage instructions
VAGUE_DOSAGE_RE = re.compile(
    r"(?<!\w)(?:uống\s+khi\s+cần|uống\s+tùy\s+ý|uống\s+tùy\s+thích|ngày\s+(?:uống\s+)?vài\s+lần|uống\s+theo\s+ý\s+thích|dùng\s+tùy\s+ý|dùng\s+khi\s+thấy\s+thích|uống\s+khi\s+nào\s+thấy\s+mệt)(?!\w)",
    re.IGNORECASE,
)
DOSAGE_UNITS_RE = re.compile(
    r"(?<!\w)(?:viên|ml|mg|g|gói|ống|chai|giọt|lần/ngày|lần\s*/\s*ngày)(?!\w)",
    re.IGNORECASE,
)
TIMING_ROUTE_RE = re.compile(
    r"(?<!\w)(?:trước\s+ăn|sau\s+ăn|trong\s+bữa\s+ăn|uống\s+sáng|uống\s+tối|tiêm|uống|ngậm|dùng\s+ngoài)(?!\w)",
    re.IGNORECASE,
)
PRESCRIPTION_WARNING_RE = re.compile(
    r"(?<!\w)(?:tái\s+khám\s+ngay\s+nếu|liên\s+hệ\s+bác\s+sĩ|dấu\s+hiệu\s+bất\s+thường|ngừng\s+thuốc\s+và\s+báo|tác\s+dụng\s+phụ|liên\s+hệ\s+ngay\s+cơ\s+sở\s+y\s+tế)(?!\w)",
    re.IGNORECASE,
)

# MED005: Prohibited testimonials / endorsements in healthcare & TPCN
TESTIMONIAL_ENDORSEMENT_RE = re.compile(
    r"(?<!\w)(?:thư\s+cảm\s+ơn\s+của\s+(?:bệnh\s+nhân|người\s+bệnh)|chia\s+sẻ\s+của\s+(?:bệnh\s+nhân|người\s+bệnh)\s+sau\s+khi\s+dùng|bác\s+sĩ\s+[^\n.,]{0,35}\s*khuyên\s+dùng\s+(?:thực\s+phẩm\s+(?:chức\s+năng|bảo\s+vệ\s+sức\s+khỏe)|sản\s+phẩm\s+này)\s+để\s+(?:chữa|điều\s+trị)|bác\s+sĩ\s+khuyên\s+dùng\s+thực\s+phẩm\s+chức\s+năng\s+này\s+để\s+chữa|dùng\s+hình\s+ảnh\s+bác\s+sĩ\s+để\s+quảng\s+cáo|lời\s+cảm\s+ơn\s+(?:từ|của)\s+(?:bệnh\s+nhân|người\s+bệnh)|phỏng\s+vấn\s+bệnh\s+nhân\s+đã\s+khỏi\s+bệnh\s+nhờ)(?!\w)",
    re.IGNORECASE,
)

# MED006: Stigmatizing, alarmist, or patient-blaming language
STIGMATIZING_LANGUAGE_RE = re.compile(
    r"(?<!\w)(?:bệnh\s+nhân\s+không\s+chịu\s+hợp\s+tác|người\s+bệnh\s+không\s+chịu\s+hợp\s+tác|bệnh\s+nan\s+y\s+vô\s+phương\s+cứu\s+chữa|vô\s+phương\s+cứu\s+chữa|con\s+nghiện\b|kẻ\s+tâm\s+thần\b|bệnh\s+nhân\s+tâm\s+thần\s+quậy\s+phá|bị\s+điên\b)(?!\w)",
    re.IGNORECASE,
)

# MED007: Emergency red-flag warnings in discharge summary
EMERGENCY_SIGNS_RE = re.compile(
    r"(?<!\w)(?:dấu\s+hiệu\s+cần\s+tái\s+khám\s+ngay|tái\s+khám\s+ngay\s+(?:nếu|khi)|cấp\s+cứu\s+ngay|đến\s+ngay\s+cơ\s+sở\s+y\s+tế|dấu\s+hiệu\s+nguy\s+hiểm\s+cần\s+quay\s+lại|sốt\s+cao\s+[^\n.,]{0,25}cần\s+tái\s+khám|cần\s+đến\s+ngay\s+bệnh\s+viện)(?!\w)",
    re.IGNORECASE,
)


def _is_comment_or_blank(line: str) -> bool:
    stripped = line.strip()
    return not stripped or stripped.startswith(("#", "<!--", "//"))


def check_line(ctx, lineno: int, raw: str, masked: str) -> Iterator[Tuple[str, str, int, str, str, str]]:
    """Per-line inspection for healthcare compliance, terminology, and patient comms."""
    if _is_comment_or_blank(raw):
        return

    # MED002: Prohibited curative or therapeutic absolute claims (fires unconditionally)
    for regex in CURATIVE_COMPILED:
        for match in regex.finditer(masked):
            yield (
                "MED002",
                ERROR,
                match.start() + 1,
                match.group(0),
                f"prohibited curative/absolute claim “{match.group(0)}”",
                "Luật Khám bệnh, chữa bệnh 2023, Luật Dược 2016 và Nghị định 15/2018/NĐ-CP nghiêm cấm cam kết khỏi bệnh 100%, quảng cáo TPCN như thuốc chữa bệnh hoặc dùng từ ngữ 'thần dược', 'điều trị dứt điểm vĩnh viễn'.",
            )

    # MED003: Obsolete licensing terminology
    for match in OBSOLETE_LICENSE_RE.finditer(masked):
        yield (
            "MED003",
            WARN,
            match.start() + 1,
            match.group(0),
            f"obsolete licensing terminology “{match.group(0)}”",
            "Luật Khám bệnh, chữa bệnh 2023 (số 15/2023/QH15, có hiệu lực từ 01/01/2024) bãi bỏ thuật ngữ 'Chứng chỉ hành nghề', thay thế bằng 'Giấy phép hành nghề khám bệnh, chữa bệnh' (hoặc 'Giấy phép hành nghề').",
        )

    # MED004: Vague dosage instructions (in prescription or healthcare advice)
    for match in VAGUE_DOSAGE_RE.finditer(masked):
        yield (
            "MED004",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"vague dosage instruction “{match.group(0)}”",
            "Thông tư 52/2017/TT-BYT & Thông tư 27/2021/TT-BYT yêu cầu ghi rõ liều lượng, số lần dùng, đường dùng, thời điểm dùng (trước/sau ăn), không được hướng dẫn chung chung 'uống khi cần' hoặc 'uống tùy ý'.",
        )

    # MED005: Prohibited patient testimonials / doctor endorsements
    if ctx.doctype in ("tpcn-ad", "clinic-landing", None):
        for match in TESTIMONIAL_ENDORSEMENT_RE.finditer(masked):
            yield (
                "MED005",
                ERROR,
                match.start() + 1,
                match.group(0),
                f"prohibited endorsement/testimonial tactic “{match.group(0)}”",
                "Nghị định 15/2018/NĐ-CP Điều 27 khoản 2 và Luật Quảng cáo 2012 nghiêm cấm sử dụng thư cảm ơn của bệnh nhân, hình ảnh hoặc lời khuyên của bác sĩ/nhân viên y tế để quảng cáo thực phẩm bảo vệ sức khỏe hoặc dịch vụ khám chữa bệnh.",
            )

    # MED006: Stigmatizing, alarmist, or patient-blaming language
    for match in STIGMATIZING_LANGUAGE_RE.finditer(masked):
        yield (
            "MED006",
            WARN,
            match.start() + 1,
            match.group(0),
            f"stigmatizing or blaming language “{match.group(0)}”",
            "Trong giao tiếp y tế và hồ sơ bệnh án, sử dụng ngôn từ nhân văn, tôn trọng người bệnh: thay 'bệnh nhân không chịu hợp tác' bằng 'người bệnh chưa phối hợp tuân thủ điều trị'; thay 'con nghiện' bằng 'người điều trị nghiện chất'; thay 'bệnh nan y vô phương cứu chữa' bằng 'tiên lượng dè dặt'.",
        )


def check_document(ctx) -> Iterator[Tuple[str, str, int, int, str, str, str]]:
    """Whole-document statutory and structural verification for healthcare documents."""
    doctype = ctx.doctype
    body = "\n".join(ctx.masked)
    if not body.strip():
        return

    first_line = next(
        (i for i, raw in enumerate(ctx.lines, 1) if not _is_comment_or_blank(raw)),
        1,
    )

    # MED001: Mandatory statutory disclaimer in TPCN advertising
    if doctype == "tpcn-ad":
        if not TPCN_DISCLAIMER_RE.search(body):
            yield (
                "MED001",
                ERROR,
                first_line,
                1,
                "",
                "quảng cáo/mô tả TPCN thiếu câu khuyến cáo bắt buộc theo Nghị định 15/2018/NĐ-CP",
                "Nghị định 15/2018/NĐ-CP Điều 27 quy định mọi quảng cáo Thực phẩm bảo vệ sức khỏe phải ghi rõ: 'Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh'.",
            )

    # MED004: Prescription missing explicit dosage units/timing or warning instructions
    if doctype == "prescription":
        has_units = bool(DOSAGE_UNITS_RE.search(body))
        has_timing = bool(TIMING_ROUTE_RE.search(body))
        has_warning = bool(PRESCRIPTION_WARNING_RE.search(body))

        if not (has_units and has_timing):
            yield (
                "MED004",
                ERROR,
                first_line,
                1,
                "",
                "đơn thuốc thiếu thông tin liều lượng, đơn vị tính hoặc thời điểm dùng rõ ràng",
                "Thông tư 52/2017/TT-BYT & TT 27/2021/TT-BYT yêu cầu đơn thuốc phải ghi rõ đơn vị tính (viên, ml, mg, gói), số lần dùng (lần/ngày) và thời điểm dùng (trước ăn / sau ăn).",
            )
        if not has_warning:
            yield (
                "MED004",
                ERROR,
                first_line,
                1,
                "",
                "đơn thuốc thiếu hướng dẫn theo dõi phản ứng có hại hoặc dấu hiệu cần tái khám ngay",
                "Đơn thuốc cần có hướng dẫn: 'Tái khám ngay nếu xuất hiện dấu hiệu bất thường' hoặc liên hệ bác sĩ điều trị khi có tác dụng phụ.",
            )

    # MED007: Discharge summary missing red-flag emergency return instructions
    if doctype == "discharge-summary":
        if not EMERGENCY_SIGNS_RE.search(body):
            yield (
                "MED007",
                ERROR,
                first_line,
                1,
                "",
                "giấy ra viện / hướng dẫn xuất viện thiếu dấu hiệu cảnh báo cần tái khám ngay",
                "Thông tư 32/2023/TT-BYT yêu cầu hướng dẫn sau xuất viện phải có mục cảnh báo dấu hiệu bất thường / dấu hiệu nguy hiểm cần đến ngay cơ sở y tế cấp cứu (sốt cao, khó thở, chảy máu, đau dữ dội).",
            )
