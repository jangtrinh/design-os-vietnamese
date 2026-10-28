# -*- coding: utf-8 -*-
# synced from shared/scripts/context_matrix.py (f6b30fdbfa220a61) — edit shared/ source, not this copy
"""Parser for ``references/context-matrix.md``: writing-context presets and word lists.

Pure Python 3.9+ standard library. Sibling of ``writing_context.py`` (the CTX rules);
``validate_copy.py`` loads both by file path. Not a ``rules_*.py`` domain module.

The caller passes ``validate_copy``'s own table parser and unwrapper so the markdown
table format has a single implementation.
"""
from __future__ import annotations

from typing import Callable, Dict, List, Sequence, Tuple

TableParser = Callable[[str, str], Tuple[List[str], List[List[str]]]]
Unwrap = Callable[[str], str]


class ContextProfile:
    """One row of the ``contexts`` table: facets, expected terms, and rule switches."""

    __slots__ = (
        "id", "label", "relation", "closeness", "channel", "purpose", "reader",
        "self_terms", "address_terms", "forbids", "disables", "enables", "basis",
    )

    def __init__(self, **fields: object) -> None:
        for name in self.__slots__:
            setattr(self, name, fields.get(name, ()))


class ContextMatrix:
    """Parsed ``context-matrix.md``: presets plus the word lists the rules read."""

    def __init__(self) -> None:
        self.profiles: Dict[str, ContextProfile] = {}
        # (token, meaning, ambiguous, caps)
        self.abbreviations: List[Tuple[str, str, bool, bool]] = []
        self.particles: List[str] = []
        self.greetings: List[str] = []
        self.greeting_endings: List[str] = []
        self.formal_openers: List[str] = []
        self.signoffs: List[str] = []
        self.summary_markers: List[str] = []


def _terms(cell: str, unwrap: Unwrap) -> Tuple[str, ...]:
    out = []
    for part in cell.split(","):
        value = unwrap(part)
        if value and value != "—":
            out.append(value)
    return tuple(out)


def _column(header: Sequence[str], name: str) -> int:
    return header.index(name) if name in header else -1


def _cell(row: Sequence[str], index: int) -> str:
    return row[index] if 0 <= index < len(row) else ""


def parse_matrix(text: str, table_with_header: TableParser, unwrap: Unwrap) -> ContextMatrix:
    """Build a :class:`ContextMatrix` from the markdown text of ``context-matrix.md``."""
    matrix = ContextMatrix()
    header, rows = table_with_header(text, "<!-- machine-readable: contexts -->")
    cols = {name: _column(header, name) for name in (
        "context", "label", "relation", "closeness", "channel", "purpose", "reader",
        "self", "address", "forbids", "disables", "enables", "basis",
    )}
    for row in rows:
        ident = unwrap(_cell(row, cols["context"]))
        if not ident or cols["relation"] < 0:
            continue
        matrix.profiles[ident] = ContextProfile(
            id=ident,
            label=_cell(row, cols["label"]),
            relation=unwrap(_cell(row, cols["relation"])),
            closeness=unwrap(_cell(row, cols["closeness"])),
            channel=unwrap(_cell(row, cols["channel"])),
            purpose=unwrap(_cell(row, cols["purpose"])),
            reader=unwrap(_cell(row, cols["reader"])),
            self_terms=_terms(_cell(row, cols["self"]), unwrap),
            address_terms=_terms(_cell(row, cols["address"]), unwrap),
            forbids=_terms(_cell(row, cols["forbids"]), unwrap),
            disables=frozenset(t.upper() for t in _terms(_cell(row, cols["disables"]), unwrap)),
            enables=frozenset(t.upper() for t in _terms(_cell(row, cols["enables"]), unwrap)),
            basis=unwrap(_cell(row, cols["basis"])),
        )

    def single_column(marker: str) -> List[str]:
        _h, data = table_with_header(text, marker)
        return [unwrap(r[0]) for r in data if r and unwrap(r[0])]

    abbr_header, abbr_rows = table_with_header(text, "<!-- machine-readable: chat-abbreviations -->")
    amb = _column(abbr_header, "ambiguous")
    caps = _column(abbr_header, "caps")
    for row in abbr_rows:
        token = unwrap(row[0]) if row else ""
        if token:
            matrix.abbreviations.append((
                token,
                _cell(row, 1),
                unwrap(_cell(row, amb)).lower() == "yes",
                unwrap(_cell(row, caps)).lower() == "yes",
            ))
    matrix.particles = single_column("<!-- machine-readable: politeness-particles -->")
    matrix.greetings = single_column("<!-- machine-readable: email-greetings -->")
    matrix.greeting_endings = single_column("<!-- machine-readable: email-greeting-endings -->")
    matrix.formal_openers = single_column("<!-- machine-readable: formal-openers -->")
    matrix.signoffs = single_column("<!-- machine-readable: email-signoffs -->")
    matrix.summary_markers = single_column("<!-- machine-readable: summary-markers -->")
    return matrix
