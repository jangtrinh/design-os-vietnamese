# -*- coding: utf-8 -*-
"""Rules for Vietnamese e-Government, online public services, and VNeID identity compliance.

Loaded automatically by validate_copy.py because the filename starts with `rules_`.
Pure Python standard library only.

This module enforces administrative and statutory compliance across Vietnamese online
public service guidelines (Nghị định 42/2022/NĐ-CP), VNeID electronic identification
and Citizen Identity Card regulations (Luật Căn cước 2023 & Nghị định 69/2024/NĐ-CP),
residence verification standards (Luật Cư trú 2020 & Nghị định 104/2022/NĐ-CP), and
administrative clerical communications (Nghị định 30/2020/NĐ-CP).
"""
from __future__ import annotations

import pathlib
import re
from typing import Iterator, Tuple

ERROR = "error"
WARN = "warning"

REF_DIR = pathlib.Path(__file__).resolve().parent.parent / "references"

DOCTYPES = {
    "dvc-guide": "Hướng dẫn Thủ tục hành chính (TTHC) trên Cổng Dịch vụ công Quốc gia (Nghị định 42/2022/NĐ-CP)",
    "vneid-notice": "Thông báo định danh điện tử VNeID & Thẻ căn cước (Luật Căn cước 2023 & Nghị định 69/2024/NĐ-CP)",
    "citizen-notification": "Thông báo giải quyết hồ sơ hành chính gửi công dân / tổ chức (Nghị định 30/2020/NĐ-CP)",
}

RULE_DOCS = {
    "GOV001": "obsolete 4-tier online public service terminology ('Dịch vụ công trực tuyến mức độ 1/2/3/4', 'DVC mức 3/4') replaced under Article 11 of Decree 42/2022/NĐ-CP by 'Dịch vụ công trực tuyến toàn trình' and 'Dịch vụ công trực tuyến một phần'",
    "GOV002": "outdated identity card terminology ('Chứng minh nhân dân 9 số còn hiệu lực', 'nộp bản sao CMND 9 số', 'cấp mới thẻ CCCD gắn chip') without noting the transition to 'Thẻ căn cước' under Law on Identification 26/2023/QH15 effective 01/07/2024 and expiration of all 9-digit CMND from 01/01/2025",
    "GOV003": "invalid VNeID electronic identity level terminology ('VNeID mức độ 3', 'VNeID mức độ 4', 'Tài khoản định danh điện tử cấp 3', 'VNeID hạng vàng') violating Decree 69/2024/NĐ-CP which defines strictly two levels: Level 1 and Level 2",
    "GOV004": "unlawful administrative requirement demanding citizens submit paper household registration books ('yêu cầu nộp Sổ hộ khẩu giấy', 'bắt buộc xuất trình Sổ hộ khẩu bản gốc', 'nộp bản sao công chứng Sổ hộ khẩu hoặc Sổ tạm trú giấy') abolished under Article 38 of Law on Residence 2020 and Decree 104/2022/NĐ-CP",
    "GOV005": "administrative procedure guide ('doctype == dvc-guide') missing mandatory statutory TTHC fields ('Trình tự thực hiện' / 'Cách thức thực hiện', 'Thành phần hồ sơ', and 'Thời hạn giải quyết')",
    "GOV006": "bureaucratic scolding, coercive threats, or machine-translated calques in citizen-facing public service portals ('Công dân tự chịu hoàn toàn hậu quả', 'Cấm hỏi nhiều tại quầy một cửa', 'Dịch vụ công cộng trên đường dây', 'Cửa hàng một điểm dừng')",
}

# GOV001: Obsolete 4-level public services
OBSOLETE_DVC_RE = re.compile(
    r"(?<!\w)(?:"
    r"dịch\s+vụ\s+công(?:\s+trực\s+tuyến)?\s+(?:mức\s+độ|mức)\s+[1-4]|"
    r"dvc(?:\s+trực\s+tuyến)?\s+(?:mức\s+độ|mức)\s+[1-4]|"
    r"dvc\s+mức\s+[1-4]|"
    r"dịch\s+vụ\s+công\s+mức\s+[1-4]"
    r")(?!\w)",
    re.IGNORECASE,
)

# GOV002: Outdated identity card terminology
OUTDATED_ID_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:chứng\s+minh\s+nhân\s+dân|cmnd)(?:\s+\(cmnd\))?\s+9\s+số(?:\s+còn\s+hiệu\s+lực)?|"
    r"(?:nộp|xuất\s+trình|bản\s+sao)\s+(?:bản\s+sao\s+)?(?:cmnd|chứng\s+minh\s+nhân\s+dân)\s+9\s+số|"
    r"cấp\s+mới\s+thẻ\s+cccd(?:\s+gắn\s+chip)?"
    r")(?!\w)",
    re.IGNORECASE,
)

# GOV003: Invalid VNeID levels
INVALID_VNEID_LEVEL_RE = re.compile(
    r"(?<!\w)(?:"
    r"vneid\s+(?:mức\s+độ|mức|cấp)\s+[3-9]|"
    r"vneid\s+hạng\s+(?:vàng|bạc|đồng|kim\s+cương|vip)|"
    r"tài\s+khoản\s+định\s+danh(?:\s+điện\s+tử)?\s+(?:mức\s+độ|mức|cấp)\s+[3-9]|"
    r"định\s+danh\s+điện\s+tử\s+(?:mức\s+độ|mức|cấp)\s+[3-9]|"
    r"tài\s+khoản\s+vneid\s+cấp\s+[3-9]"
    r")(?!\w)",
    re.IGNORECASE,
)

# GOV004: Demanding paper household registration books
PAPER_HOKHAU_DEMAND_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:yêu\s+cầu|bắt\s+buộc|phải|cần)\s+(?:công\s+dân\s+)?(?:nộp|xuất\s+trình|cung\s+cấp)\s+[^\n.,;:]*?(?:sổ\s+hộ\s+khẩu|sổ\s+tạm\s+trú)(?:\s+giấy|\s+bản\s+gốc)?|"
    r"(?:nộp|xuất\s+trình)\s+(?:bản\s+sao(?:\s+công\s+chứng)?\s+)?(?:sổ\s+hộ\s+khẩu|sổ\s+tạm\s+trú)(?:\s+giấy|\s+bản\s+gốc)|"
    r"(?:sổ\s+hộ\s+khẩu|sổ\s+tạm\s+trú)\s+giấy|"
    r"sổ\s+hộ\s+khẩu\s+bản\s+gốc"
    r")(?!\w)",
    re.IGNORECASE,
)

# GOV006: Bureaucratic scolding, coercive threats, and machine-translated administrative calques
BUREAUCRATIC_COERCION_RE = re.compile(
    r"(?<!\w)(?:"
    r"công\s+dân\s+tự\s+chịu\s+(?:hoàn\s+toàn\s+)?hậu\s+quả|"
    r"tự\s+chịu\s+(?:hoàn\s+toàn\s+)?hậu\s+quả\s+nếu\s+không\s+biết\s+thao\s+tác|"
    r"cấm\s+hỏi\s+nhiều(?:\s+tại\s+quầy\s+một\s+cửa)?|"
    r"cán\s+bộ\s+không\s+có\s+nghĩa\s+vụ\s+giải\s+thích|"
    r"không\s+tiếp\s+công\s+dân\s+hỏi\s+quá\s+\d+|"
    r"dịch\s+vụ\s+công\s+cộng\s+trên\s+đường\s+dây|"
    r"cửa\s+hàng\s+một\s+điểm\s+dừng|"
    r"bàn\s+dịch\s+vụ\s+công\s+dân"
    r")(?!\w)",
    re.IGNORECASE,
)

# Structural markers for dvc-guide (GOV005)
PROCEDURE_RE = re.compile(
    r"(?<!\w)(?:trình\s+tự\s+thực\s+hiện|cách\s+thức\s+thực\s+hiện)(?!\w)",
    re.IGNORECASE,
)
DOSSIER_RE = re.compile(
    r"(?<!\w)thành\s+phần\s+hồ\s+sơ(?!\w)",
    re.IGNORECASE,
)
TIMELINE_RE = re.compile(
    r"(?<!\w)thời\s+hạn\s+giải\s+quyết(?!\w)",
    re.IGNORECASE,
)


def _is_comment_or_blank(line: str) -> bool:
    stripped = line.strip()
    return not stripped or stripped.startswith(("#", "<!--", "//"))


def _is_negated(text: str, start: int) -> bool:
    prefix = text[max(0, start - 60):start].lower()
    return any(neg in prefix for neg in (
        "không yêu cầu", "không bắt buộc", "không cần", "không được yêu cầu",
        "bãi bỏ", "thay cho", "thay thế", "nghiêm cấm", "cấm", "hết hạn", "bãi bỏ việc",
    ))


def check_line(ctx, lineno: int, raw: str, masked: str) -> Iterator[Tuple[str, str, int, str, str, str]]:
    if _is_comment_or_blank(raw):
        return

    # GOV001: Obsolete 4-level public service classification
    for match in OBSOLETE_DVC_RE.finditer(masked):
        yield (
            "GOV001",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"obsolete online public service tier “{match.group(0)}” replaced under Article 11 of Decree 42/2022/NĐ-CP",
            "replace 4-level classification (mức độ 1-4) with exactly two statutory tiers: 'Dịch vụ công trực tuyến toàn trình' (full-process) or 'Dịch vụ công trực tuyến một phần' (partial)",
        )

    # GOV002: Outdated identity card terminology
    for match in OUTDATED_ID_RE.finditer(masked):
        if _is_negated(masked, match.start()):
            continue
        yield (
            "GOV002",
            WARN,
            match.start() + 1,
            match.group(0),
            f"outdated identity card terminology “{match.group(0)}”",
            "under Law on Identification 26/2023/QH15 effective 01/07/2024, newly issued cards are titled 'Thẻ căn cước'; legacy 9-digit CMND expired after 31/12/2024",
        )

    # GOV003: Invalid VNeID electronic identity levels
    for match in INVALID_VNEID_LEVEL_RE.finditer(masked):
        yield (
            "GOV003",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"invalid VNeID electronic identity level “{match.group(0)}”",
            "Decree 69/2024/NĐ-CP defines strictly two electronic identity levels: 'Tài khoản định danh điện tử mức độ 1' and 'Tài khoản định danh điện tử mức độ 2'",
        )

    # GOV004: Unlawful administrative requirement demanding paper household books
    for match in PAPER_HOKHAU_DEMAND_RE.finditer(masked):
        if _is_negated(masked, match.start()):
            continue
        yield (
            "GOV004",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"unlawful requirement demanding paper household registration book “{match.group(0)}”",
            "Sổ hộ khẩu giấy and Sổ tạm trú giấy were abolished from 01/01/2023 under Article 38 Law on Residence 2020 and Decree 104/2022/NĐ-CP; verify residence via VNeID Level 2, National Population Database, or Form CT07",
        )

    # GOV006: Bureaucratic scolding, coercive threats, or machine-translated administrative calques
    for match in BUREAUCRATIC_COERCION_RE.finditer(masked):
        yield (
            "GOV006",
            WARN,
            match.start() + 1,
            match.group(0),
            f"bureaucratic scolding, threat, or mistranslated administrative term “{match.group(0)}”",
            "maintain courteous civil service language under Decree 30/2020/NĐ-CP; use standard administrative terms (e.g. 'Dịch vụ công trực tuyến', 'Bộ phận Một cửa / Trung tâm Phục vụ hành chính công')",
        )


def check_document(ctx) -> Iterator[Tuple[str, str, int, int, str, str, str]]:
    doctype = ctx.doctype
    body = "\n".join(ctx.masked)
    if not body.strip():
        return

    first_line = next((i for i, raw in enumerate(ctx.lines, 1) if not _is_comment_or_blank(raw)), 1)

    # GOV005: Missing mandatory statutory TTHC fields in dvc-guide
    if doctype == "dvc-guide":
        has_procedure = bool(PROCEDURE_RE.search(body))
        has_dossier = bool(DOSSIER_RE.search(body))
        has_timeline = bool(TIMELINE_RE.search(body))

        if not (has_procedure and has_dossier and has_timeline):
            missing_fields = []
            if not has_procedure:
                missing_fields.append("'Trình tự thực hiện' hoặc 'Cách thức thực hiện'")
            if not has_dossier:
                missing_fields.append("'Thành phần hồ sơ'")
            if not has_timeline:
                missing_fields.append("'Thời hạn giải quyết'")
            yield (
                "GOV005",
                ERROR,
                first_line,
                1,
                "",
                f"dvc-guide missing mandatory statutory administrative procedure fields: {'; '.join(missing_fields)}",
                "administrative procedure guides (TTHC) under Decree 42/2022/NĐ-CP must explicitly provide Trình tự thực hiện, Thành phần hồ sơ, and Thời hạn giải quyết",
            )
