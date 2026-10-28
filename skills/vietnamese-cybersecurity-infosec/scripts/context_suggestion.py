# -*- coding: utf-8 -*-
# synced from shared/scripts/context_suggestion.py (00a488aa3e3c4262) — edit shared/ source, not this copy
"""Writing-context suggestion for ``validate_copy.py`` (a stderr hint, never a finding).

Pure Python 3.9+ standard library. Sibling of ``writing_context.py``; loaded by file
path. The heuristics are deliberately narrow: an opener-plus-self-term pattern at the
very start of the text, and silence for style guides, organisation notices and
markdown documents. A missed hint costs nothing; a wrong hint is noise.
"""
from __future__ import annotations

import re
from typing import List, Optional

_HEAD_LINES = 5
_APPLY_LINES = 8

_FORMAL_OPENER = r"(?:kính\s+gửi|kính\s+thưa|thưa|dear)"
_MANAGER_OPENER_RE = re.compile(rf"^[ \t>*_-]*{_FORMAL_OPENER}\s+(?:anh|chị|sếp)(?!\w)", re.IGNORECASE)
_LETTER_OPENER_RE = re.compile(rf"^[ \t>*_-]*{_FORMAL_OPENER}(?!\w)", re.IGNORECASE)
_SELF_EM_RE = re.compile(
    r"(?<!\w)em\s+(?:xin|gửi|là|rất|đã|sẽ|muốn|cảm\s+ơn|kính|mong|báo\s+cáo|nhờ)(?!\w)",
    re.IGNORECASE,
)
_APPLY_RE = re.compile(
    r"(?<!\w)(?:tôi|em|mình)\s+(?:rất\s+)?(?:(?:xin|muốn|mong|được)\s+)*"
    r"(?:ứng\s+tuyển|nộp\s+hồ\s+sơ|xin\s+việc)(?!\w)"
    r"|(?<!\w)(?:đính\s+kèm|gửi\s+kèm|kèm\s+theo)\s+CV(?!\w)",
    re.IGNORECASE,
)
# An organisation writing to customers or candidates, or text that talks about letters.
_ORGANISATION_RE = re.compile(
    r"(?<!\w)(?:chúng\s+tôi|quý\s+khách|quý\s+vị|chăm\s+sóc\s+khách\s+hàng|đơn\s+hàng|"
    r"trân\s+trọng\s+thông\s+báo|thông\s+báo\s+kết\s+quả|phòng\s+nhân\s+sự|bộ\s+phận|"
    r"các\s+ứng\s+viên|mẫu\s+thư|ví\s+dụ)(?!\w)",
    re.IGNORECASE,
)
_QUOTED_RE = re.compile(r"“[^”]*”|\"[^\"\n]*\"|`[^`\n]*`|‘[^’]*’")
_META_RE = re.compile(
    r"(?<!\w)(?:tránh|không\s+nên|đừng|cấm|quy\s+tắc|hướng\s+dẫn|người\s+ta|đại\s+từ|xưng\s+hô|thay\s+vì)(?!\w)",
    re.IGNORECASE,
)
_MAY_RE = re.compile(r"(?<!\w)mày(?!\w)", re.IGNORECASE)
_TAO_RE = re.compile(r"(?<!\w)tao(?!\w)", re.IGNORECASE)
_NAMING_VERB_RE = re.compile(r"(?:dùng|xưng|gọi|từ|chữ|cụm\s+từ)\s+(?:mày|tao)(?!\w)", re.IGNORECASE)
_MARKDOWN_STRUCTURE_RE = re.compile(r"^\s*(?:#|\|)", re.MULTILINE)


def _first_lines(text: str, count: int) -> List[str]:
    return [line.strip() for line in text.splitlines() if line.strip()][:count]


def suggest_context(text: str) -> Optional[str]:
    """Return a preset id when strong signals appear at the start of ``text``, else ``None``."""
    lines = _first_lines(text, _APPLY_LINES)
    if not lines or _MARKDOWN_STRUCTURE_RE.search(text) or _ORGANISATION_RE.search(text):
        return None
    first = lines[0]
    if _LETTER_OPENER_RE.match(first) and _APPLY_RE.search(" ".join(lines)):
        return "job-application"
    if _MANAGER_OPENER_RE.match(first) and _SELF_EM_RE.search(" ".join(lines[:_HEAD_LINES])):
        return "email-to-manager"
    spoken = _QUOTED_RE.sub(" ", " ".join(lines[:3]))
    if _META_RE.search(spoken) or _NAMING_VERB_RE.search(spoken):
        return None
    if _MAY_RE.search(spoken) and _TAO_RE.search(spoken):
        return "chat-close-friend"
    return None
