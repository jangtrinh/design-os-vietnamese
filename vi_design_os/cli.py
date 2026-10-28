"""Run the bundled ``shared/scripts/*.py`` checkers as installed console commands.

Layout contract (the scripts resolve references and domain rules relative to
their own location, so the installed tree must keep ``shared/`` and ``skills/``
as siblings):

* installed wheel      ``<site-packages>/vi_design_os/{cli.py, shared/, skills/}``
* source checkout      ``<repo>/{vi_design_os/cli.py, shared/, skills/}``
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys
from types import ModuleType
from typing import Optional, Sequence

_PACKAGE_DIR = pathlib.Path(__file__).resolve().parent


def bundle_root() -> pathlib.Path:
    """Directory that holds the ``shared/`` and ``skills/`` siblings."""
    if (_PACKAGE_DIR / "shared" / "scripts").is_dir():
        return _PACKAGE_DIR
    return _PACKAGE_DIR.parent


def _load_script(filename: str) -> ModuleType:
    path = bundle_root() / "shared" / "scripts" / filename
    if not path.is_file():
        raise SystemExit(
            f"error: bundled script not found: {path}\n"
            "reinstall design-os-vietnamese (the package data is incomplete)"
        )
    module_name = f"_vi_design_os_{path.stem}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"error: cannot load bundled script: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def _run(filename: str, argv: Optional[Sequence[str]]) -> int:
    return int(_load_script(filename).main(argv))


def validate_copy_main(argv: Optional[Sequence[str]] = None) -> int:
    """``vi-validate-copy``: same flags and exit codes as ``validate_copy.py``."""
    return _run("validate_copy.py", argv)


def i18n_parity_main(argv: Optional[Sequence[str]] = None) -> int:
    """``vi-i18n-parity``: same flags and exit codes as ``check_i18n_parity.py``."""
    return _run("check_i18n_parity.py", argv)


def font_coverage_main(argv: Optional[Sequence[str]] = None) -> int:
    """``vi-font-coverage``: same flags and exit codes as ``check_font_coverage.py``."""
    return _run("check_font_coverage.py", argv)
