"""Console entry points for the DESIGN:OS Vietnamese linters.

The three checkers live as standalone stdlib scripts in ``shared/scripts/`` so
every skill folder can stay self-contained. This package only locates those
scripts and runs them, which keeps a single implementation for the agent-skill
copies, the pip-installed commands and the pre-commit hooks.
"""

__all__ = ["cli"]
