# -*- coding: utf-8 -*-
"""Rules for Vietnamese media, journalism, press releases, corrections, and crisis PR compliance.

Loaded automatically by validate_copy.py because the filename starts with `rules_`.
Pure Python standard library only.

This module enforces statutory and professional journalism standards under the Press Law 2016
(Luật Báo chí 2016), Decree 147/2024/NĐ-CP on Internet services and online information,
constitutional presumption of innocence (Hiến pháp 2013 Điều 31 & Bộ luật Tố tụng hình sự 2015),
anonymization of children under 16 (Luật Trẻ em 2016 Điều 21 & Nghị định 56/2017/NĐ-CP),
press correction and apology requirements (Điều 42 Luật Báo chí), professional press release
architecture, and constructive crisis communications.
"""
from __future__ import annotations

import pathlib
import re
from typing import Iterator, Tuple

ERROR = "error"
WARN = "warning"

REF_DIR = pathlib.Path(__file__).resolve().parent.parent / "references"

DOCTYPES = {
    "press-release": "Thông cáo báo chí chính thức (Press Release — Luật Báo chí 2016)",
    "correction-apology": "Thông báo Cải chính & Xin lỗi trên báo chí (Điều 42 Luật Báo chí 2016)",
    "crisis-statement": "Thông cáo xử lý khủng hoảng truyền thông (Crisis Communications Statement)",
}

RULE_DOCS = {
    "MEDJ001": "general news website (ICP) or social media page claiming press agency status or conducting unauthorized investigative journalism (Luật Báo chí 2016 & Nghị định 147/2024/NĐ-CP)",
    "MEDJ002": "press correction notice missing explicit correction & apology ('Cải chính' / 'Xin lỗi') and original publication details, or asserting silent article deletion without formal correction under Article 42 Press Law 2016",
    "MEDJ003": "violating presumption of innocence by labeling suspect/indicted person a criminal/murderer before legally effective court judgment (Hiến pháp 2013 Điều 31 & Bộ luật Tố tụng hình sự 2015 Điều 13)",
    "MEDJ004": "revealing identity, unblurred face, or school address of a child under 16 in media coverage violating Article 21 Law on Children 2016 (Luật Trẻ em 2016 & Nghị định 56/2017/NĐ-CP)",
    "MEDJ005": "journalism/PR English calques ('Để phát hành ngay lập tức', 'Trên hồ sơ', 'Ngoài hồ sơ', 'Câu chuyện dẫn đầu', 'Người giữ cổng thông tin', 'Dòng chữ ký của tác giả'), or press release missing dateline/media contact",
    "MEDJ006": "hostile, retaliatory, or victim-blaming crisis PR statements threatening lawsuits against consumers without verification or disclaiming company duty of explanation",
}

# MEDJ001: ICP claiming press status or self-producing investigative journalism
ICP_PRESS_PRETENSE_RE = re.compile(
    r"(?<!\w)(?:"
    r"trang\s+thông\s+tin\s+điện\s+tử\s+tổng\s+hợp(?:\s+[^\n.,;]*?)?\s+tự\s+sản\s+xuất\s+tin\s+bài(?:\s+điều\s+tra)?(?:\s+như\s+cơ\s+quan\s+báo\s+chí)?|"
    r"tòa\s+soạn\s+báo\s+điện\s+tử\s+thuộc\s+giấy\s+phép\s+icp(?:\s+mạng\s+xã\s+hội)?|"
    r"trang\s+thông\s+tin\s+điện\s+tử\s+tổng\s+hợp(?:\s+[^\n.,;]*?)?\s+hoạt\s+động\s+như\s+cơ\s+quan\s+báo\s+chí|"
    r"tòa\s+soạn\s+chuyên\s+trang\s+trực\s+thuộc\s+trang\s+thông\s+tin\s+điện\s+tử\s+tổng\s+hợp|"
    r"giấy\s+phép\s+icp(?:\s+[^\n.,;]*?)?\s+xuất\s+bản\s+báo\s+chí"
    r")(?!\w)",
    re.IGNORECASE,
)

# MEDJ002: Asserting silent deletion without formal correction
SILENT_DELETION_RE = re.compile(
    r"(?<!\w)(?:"
    r"chỉ\s+cần\s+gỡ\s+bài(?:\s+âm\s+thầm)?(?:\s+không\s+cần\s+đăng\s+thông\s+báo)?(?:\s+cải\s+chính)?(?:\s+xin\s+lỗi)?|"
    r"gỡ\s+bài(?:\s+khỏi\s+hệ\s+thống)?\s+mà\s+không\s+cần\s+(?:đăng\s+)?cải\s+chính(?:\s+xin\s+lỗi)?|"
    r"âm\s+thầm\s+gỡ\s+bỏ\s+bài\s+viết(?:\s+sai\s+sự\s+thật)?\s+mà\s+không\s+xin\s+lỗi"
    r")(?!\w)",
    re.IGNORECASE,
)

# MEDJ003: Violating presumption of innocence before conviction
INNOCENCE_VIOLATION_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:tên\s+tội\s+phạm|hung\s+thủ|kẻ\s+giết\s+người|kẻ\s+lừa\s+đảo|kẻ\s+cướp|kẻ\s+phạm\s+tội)\s+[^\n.,;]*?(?:vừa\s+bị|đã\s+bị|bị)\s+(?:tạm\s+giữ|khởi\s+tố|triệu\s+tập|bắt\s+giữ|điều\s+tra)(?:\s+[^\n.,;]*?)?(?:khi\s+chưa\s+xét\s+xử|để\s+điều\s+tra|lấy\s+lời\s+khai)?|"
    r"(?:tên\s+tội\s+phạm|hung\s+thủ|kẻ\s+giết\s+người|kẻ\s+lừa\s+đảo)\s+[A-ZÀ-Ỹ][a-zà-ỹ]+(?:\s+[A-ZÀ-Ỹ][a-zà-ỹ]+){1,4}\s+(?:vừa\s+bị|đã\s+bị|bị)|"
    r"(?:khởi\s+tố|tạm\s+giữ|bắt\s+tạm\s+giam)\s+(?:tên\s+tội\s+phạm|hung\s+thủ|kẻ\s+giết\s+người|kẻ\s+lừa\s+đảo)"
    r")(?!\w)",
    re.IGNORECASE,
)

# MEDJ004: Children under 16 identity disclosure
CHILD_IDENTITY_VIOLATION_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:công\s+khai\s+rõ\s+mặt|đăng\s+ảnh\s+cận\s+mặt|tiết\s+lộ\s+danh\s+tính|nêu\s+rõ\s+danh\s+tính|công\s+khai\s+danh\s+tính)[^\n.,;]*?(?:trẻ\s+em|cháu\s+bé|học\s+sinh)\s+(?:\d{1,2}\s+tuổi|dưới\s+16\s+tuổi)|"
    r"(?:họ\s+tên\s+đầy\s+đủ\s+và\s+địa\s+chỉ\s+trường\s+lớp\s+của\s+(?:cháu\s+bé|trẻ\s+em|học\s+sinh)\s+\d{1,2}\s+tuổi)|"
    r"đăng\s+ảnh\s+cận\s+mặt\s+trẻ\s+em\s+\d{1,2}\s+tuổi\s+không\s+làm\s+mờ|"
    r"công\s+khai\s+rõ\s+mặt,\s*họ\s+tên\s+đầy\s+đủ\s+và\s+địa\s+chỉ\s+trường\s+lớp\s+của\s+cháu\s+bé|"
    r"công\s+khai\s+danh\s+tính\s+và\s+hình\s+ảnh\s+của\s+trẻ\s+em\s+dưới\s+16\s+tuổi"
    r")(?!\w)",
    re.IGNORECASE,
)

# MEDJ005: Media / PR English calques
MEDIA_CALQUES: Tuple[Tuple[re.Pattern, str, str], ...] = (
    (
        re.compile(r"(?<!\w)để\s+phát\s+hành\s+ngay\s+lập\s+tức(?!\w)", re.IGNORECASE),
        "Để phát hành ngay lập tức",
        "Thông cáo báo chí phát hành ngay",
    ),
    (
        re.compile(r"(?<!\w)trên\s+hồ\s+sơ(?!\w)", re.IGNORECASE),
        "Trên hồ sơ",
        "Phát ngôn chính thức / Thông tin có dẫn nguồn (on the record)",
    ),
    (
        re.compile(r"(?<!\w)ngoài\s+hồ\s+sơ(?!\w)", re.IGNORECASE),
        "Ngoài hồ sơ",
        "Thông tin hậu trường không trích dẫn / Thông tin ngoài lề (off the record)",
    ),
    (
        re.compile(r"(?<!\w)câu\s+chuyện\s+dẫn\s+đầu(?!\w)", re.IGNORECASE),
        "Câu chuyện dẫn đầu",
        "Đoạn mở đầu / Sapo / Tiêu điểm (lead story)",
    ),
    (
        re.compile(r"(?<!\w)người\s+giữ\s+cổng\s+thông\s+tin(?!\w)", re.IGNORECASE),
        "Người giữ cổng thông tin",
        "Biên tập viên kiểm duyệt / Ban biên tập (gatekeeper)",
    ),
    (
        re.compile(r"(?<!\w)dòng\s+chữ\s+ký\s+của\s+tác\s+giả(?!\w)", re.IGNORECASE),
        "Dòng chữ ký của tác giả",
        "Bút danh / Tên tác giả (byline)",
    ),
)

# MEDJ006: Hostile / victim-blaming crisis statements
HOSTILE_PR_RE = re.compile(
    r"(?<!\w)(?:"
    r"khách\s+hàng\s+(?:cố\s+tình\s+)?(?:bịa\s+đặt|vu\s+khống)[^\n.,;]*?sẽ\s+bị\s+công\s+ty\s+kiện\s+đến\s+cùng|"
    r"sự\s+cố\s+hoàn\s+toàn\s+do\s+lỗi\s+(?:của\s+)?(?:người\s+tiêu\s+dùng|khách\s+hàng)\s+thiếu\s+hiểu\s+biết|"
    r"công\s+ty\s+không\s+có\s+nghĩa\s+vụ\s+giải\s+thích(?:\s+cho\s+khách\s+hàng)?|"
    r"chúng\s+tôi\s+sẽ\s+khởi\s+kiện\s+bất\s+kỳ\s+khách\s+hàng\s+nào\s+khiếu\s+nại|"
    r"khách\s+hàng\s+phải\s+tự\s+chịu\s+trách\s+nhiệm,\s*công\s+ty\s+từ\s+chối\s+đối\s+thoại"
    r")(?!\w)",
    re.IGNORECASE,
)


def _is_comment_or_blank(line: str) -> bool:
    stripped = line.strip()
    return not stripped or stripped.startswith(("#", "<!--", "//"))


META_NEGATION_RE = re.compile(
    r"(?:đã\s+bãi\s+bỏ|bãi\s+bỏ\s+quy\s+định|bãi\s+bỏ\s+loại\s+hình|thay\s+thế\s+cho|"
    r"không\s+được(?:\s+phép)?\s+(?:quảng\s+cáo|tuyên\s+bố|cam\s+kết|ghi|viết|dùng|sử\s+dụng)|"
    r"nghiêm\s+cấm\s+(?:quảng\s+cáo|tuyên\s+bố|cam\s+kết|ghi|viết|dùng|sử\s+dụng)|"
    r"cấm\s+(?:quảng\s+cáo|tuyên\s+bố|cam\s+kết)\s+|"
    r"tránh\s+(?:viết|dùng|sử\s+dụng))\s*[^\n.;:]{0,25}$",
    re.IGNORECASE,
)


def _is_negated_or_meta(raw_line: str, match_start: int) -> bool:
    prefix = raw_line[max(0, match_start - 60):match_start]
    return bool(META_NEGATION_RE.search(prefix))


def check_line(ctx, lineno: int, raw: str, masked: str) -> Iterator[Tuple[str, str, int, str, str, str]]:
    if _is_comment_or_blank(raw):
        return

    # MEDJ001: ICP claiming press agency status
    for match in ICP_PRESS_PRETENSE_RE.finditer(masked):
        yield (
            "MEDJ001",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"ICP general news website falsely claiming press agency status “{match.group(0)}”",
            "Under Press Law 2016 and Decree 147/2024/NĐ-CP, general news websites (ICP) must not pose as licensed press agencies, use terms like 'Tòa soạn báo', or self-produce investigative journalism",
        )

    # MEDJ002: Asserting silent deletion without correction notice
    for match in SILENT_DELETION_RE.finditer(masked):
        yield (
            "MEDJ002",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"asserting silent deletion without formal correction “{match.group(0)}”",
            "Article 42 of Press Law 2016 mandates that erroneous press reports must be corrected with an explicit apology published in the same section and size; silent deletion without correction is illegal",
        )

    # MEDJ003: Violating presumption of innocence
    for match in INNOCENCE_VIOLATION_RE.finditer(masked):
        yield (
            "MEDJ003",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"violating constitutional presumption of innocence: “{match.group(0)}”",
            "Article 31 of Constitution 2013 and Article 13 Criminal Procedure Code 2015 prohibit calling a person a criminal ('tên tội phạm', 'hung thủ', 'kẻ giết người') before a legally effective court judgment; use 'nghi phạm', 'đối tượng', 'bị can', or 'bị cáo'",
        )

    # MEDJ004: Revealing child identity under 16
    for match in CHILD_IDENTITY_VIOLATION_RE.finditer(masked):
        yield (
            "MEDJ004",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"revealing child identity / unblurred face in media: “{match.group(0)}”",
            "Article 21 Law on Children 2016 and Decree 56/2017/NĐ-CP prohibit publishing full names, school addresses, or unblurred faces of children under 16 without parental consent",
        )

    # MEDJ005: Journalism / PR English calques
    for regex, term, hint in MEDIA_CALQUES:
        for match in regex.finditer(masked):
            yield (
                "MEDJ005",
                WARN,
                match.start() + 1,
                match.group(0),
                f"awkward English calque in journalism/PR “{match.group(0)}”",
                f"use standard Vietnamese wording: “{hint}”",
            )

    # MEDJ006: Hostile / retaliatory crisis statements
    for match in HOSTILE_PR_RE.finditer(masked):
        yield (
            "MEDJ006",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"hostile, retaliatory, or victim-blaming crisis statement “{match.group(0)}”",
            "crisis communications must maintain empathy, state objective verification actions, and never threaten litigation against complaining consumers or disclaim duty of explanation",
        )


def check_document(ctx) -> Iterator[Tuple[str, str, int, int, str, str, str]]:
    doctype = ctx.doctype
    body = "\n".join(ctx.masked)
    if not body.strip():
        return

    first_line = next((i for i, raw in enumerate(ctx.lines, 1) if not _is_comment_or_blank(raw)), 1)

    # MEDJ002: Press correction notice missing apology or original article details
    if doctype == "correction-apology":
        has_correction = bool(re.search(r"(?<!\w)cải\s+chính(?!\w)", body, re.IGNORECASE))
        has_apology = bool(re.search(r"(?<!\w)xin\s+lỗi(?!\w)", body, re.IGNORECASE))
        has_original = bool(re.search(
            r"(?<!\w)(?:bài\s+viết|tiêu\s+đề|ngày\s+đăng|xuất\s+bản|số\s+báo)(?!\w)",
            body,
            re.IGNORECASE,
        ))

        if not (has_correction and has_apology and has_original):
            missing_items = []
            if not has_correction:
                missing_items.append("nội dung 'Cải chính'")
            if not has_apology:
                missing_items.append("lời 'Xin lỗi' bạn đọc / cơ quan / cá nhân")
            if not has_original:
                missing_items.append("thông tin bài viết gốc (tiêu đề, ngày đăng)")
            yield (
                "MEDJ002",
                ERROR,
                first_line,
                1,
                "",
                f"correction-apology missing mandatory statutory components under Article 42 Press Law 2016: {'; '.join(missing_items)}",
                "Article 42 Press Law 2016 requires formal press corrections to explicitly include correction of facts, apology, and references to the original erroneous article",
            )

    # MEDJ005: Press release missing location/dateline or media contact
    if doctype == "press-release":
        has_dateline = bool(re.search(
            r"(?<!\w)(?:Hà\s+Nội|TP\.?\s*HCM|Đà\s+Nẵng|Hải\s+Phòng|Cần\s+Thơ)[,\s]+ngày\s+\d{1,2}\s+tháng\s+\d{1,2}\s+năm\s+\d{4}|ngày\s+\d{1,2}/\d{1,2}/\d{4}",
            body,
            re.IGNORECASE,
        ))
        has_contact = bool(re.search(
            r"(?<!\w)(?:thông\s+tin\s+liên\s+hệ\s+báo\s+chí|liên\s+hệ\s+báo\s+chí|liên\s+hệ\s+truyền\s+thông|đầu\s+mối\s+liên\s+hệ|thông\s+tin\s+liên\s+hệ)(?!\w)",
            body,
            re.IGNORECASE,
        ))

        if not (has_dateline and has_contact):
            missing_items = []
            if not has_dateline:
                missing_items.append("địa điểm & ngày tháng phát hành (dateline)")
            if not has_contact:
                missing_items.append("Thông tin liên hệ báo chí / truyền thông")
            yield (
                "MEDJ005",
                WARN,
                first_line,
                1,
                "",
                f"press-release missing standard professional components: {'; '.join(missing_items)}",
                "standard press releases must include a formal location/date dateline and explicit media relations contact information",
            )
