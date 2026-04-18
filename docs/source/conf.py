from __future__ import annotations

import logging
import re
import sys
from pathlib import Path

from sphinx.application import Sphinx
from sphinx.util import logging as sphinx_logging


ROOT_DIR = Path(__file__).resolve().parents[2]
DOCS_DIR = Path(__file__).resolve().parents[1]
STUBS_DIR = DOCS_DIR / "stubs"

sys.path.insert(0, str(ROOT_DIR))


project = "MarketMind"
author = "Mark Wuenschel"
copyright = "2025-2026, Mark Wuenschel"


def extract_release(version_text: str) -> str:
    """Latest ``## Version M.m.p`` heading in VERSION.md (ledger is newest-first)."""
    pattern = re.compile(
        r"^##\s*Version\s+([0-9]+\.[0-9]+\.[0-9]+)",
        re.MULTILINE,
    )
    matches = pattern.findall(version_text)
    if not matches:
        return "0.0.0"

    def _semver_key(v: str) -> tuple[int, int, int]:
        return tuple(int(p) for p in v.split(".", 2))

    return max(matches, key=_semver_key)


VERSION_PATH = ROOT_DIR / "VERSION.md"
VERSION_TEXT = VERSION_PATH.read_text(encoding="utf-8")
release = extract_release(VERSION_TEXT)
version = ".".join(release.split(".")[:2])

html_title = f"{project} {release} Documentation"
html_short_title = f"{project} Docs"

# Local `sphinx-build -W` and CI: stub AutoAPI + mirrored Markdown emit noisy
# warnings that RTD already tolerates (`fail_on_warning: false`). Suppress
# categories so strict builds stay usable as a sync gate.
suppress_warnings = [
    "autoapi.python_import_resolution",
    "misc.highlighting_failure",
    "myst.xref_missing",
    "myst.header",
    "ref.python",
    "design.grid",
    "image.not_readable",
    "toc.not_included",
]


extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinxcontrib.autodoc_pydantic",
    "autoapi.extension",
    "sphinx.ext.autosummary",
    "sphinxcontrib.mermaid",
    "sphinx.ext.graphviz",
    "sphinx.ext.mathjax",
    "sphinx_copybutton",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx_design",
    "sphinx.ext.intersphinx",
]

myst_parser_add_suffix = False
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
    "smartquotes",
    "replacements",
    "linkify",
    "attrs_inline",
    "substitution",
    "tasklist",
    "dollarmath",
    "attrs_block",
]
myst_heading_anchors = 3

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**.ipynb_checkpoints",
    ".venv",
    ".tox",
    ".pytest_cache",
    "*.egg-info",
]

html_theme = "furo"
html_static_path = ["_static"]
html_extra_path = ["_extra", "assets"]
html_css_files = ["custom.css"]
html_theme_options = {
    "navigation_with_keys": True,
}

autodoc_pydantic_model_show_json = True
autodoc_pydantic_model_show_config_summary = True
autodoc_pydantic_model_show_field_summary = True
autodoc_pydantic_field_show_constraints = True
autodoc_pydantic_model_member_order = "bysource"
autodoc_pydantic_model_show_field_type = True
autodoc_pydantic_model_show_validator_summary = True
autodoc_pydantic_model_show_validator_regex = True
autodoc_pydantic_settings_show_config_member = True

mermaid_output_format = "svg"

autoapi_type = "python"
autoapi_add_toctree_entry = True
autoapi_dirs = [str(STUBS_DIR)]
autoapi_python_use_stub_files = True
autoapi_ignore = [
    "*/tests/*",
    "*/__init__.py",
]
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "special-members",
    "imported-members",
    "show-module-members",
]
autoapi_keep_files = True
autoapi_root = "reference"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "sklearn": ("https://scikit-learn.org/stable/", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
    "statsmodels": ("https://www.statsmodels.org/stable/", None),
    "joblib": ("https://joblib.readthedocs.io/en/latest/", None),
    "ib_insync": ("https://ib-insync.readthedocs.io/", None),
    "pydantic": ("https://docs.pydantic.dev/latest/", "https://docs.pydantic.dev/latest/objects.inv"),
    "structlog": ("https://www.structlog.org/en/stable/", None),
    "typing_extensions": ("https://typing-extensions.readthedocs.io/en/latest/", None),
    "requests": ("https://requests.readthedocs.io/en/latest/", None),
    "aiohttp": ("https://docs.aiohttp.org/en/stable/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_timeout = 30

mathjax_config = {
    "tex2jax": {
        "inlineMath": [["$", "$"], ["\\(", "\\)"]],
        "displayMath": [["$$", "$$"], ["\\[", "\\]"]],
    }
}
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
    "inherited-members": True,
    "special-members": "__init__",
}
autodoc_typehints = "description"
autodoc_typehints_format = "short"

autosummary_generate = True
autosummary_imported_members = False

todo_include_todos = True


class _SuppressAutoapiPlaceholder(logging.Filter):
    """AutoAPI logs unresolved stub placeholders without Sphinx warning types."""

    def filter(self, record: logging.LogRecord) -> bool:
        try:
            msg = record.getMessage()
        except (TypeError, ValueError, AttributeError):
            return True
        return not str(msg).startswith("Unknown type: placeholder")


def _patch_autoapi_duplicate_source(
    app: Sphinx, docname: str, source: list[str]
) -> None:
    """In-memory fixes for a few AutoAPI pages where stub expansion collides in-doc."""
    import re

    if docname == "reference/srcPy/data/ib_api/index":
        t = source[0]
        t = t.replace(
            "   srcPy.data.ib_api.IBKRConnectionError\n   srcPy.data.ib_api.IBKRConnectionError\n",
            "   srcPy.data.ib_api.IBKRConnectionError\n",
        )
        t = re.sub(
            r"\n\.\. py:exception:: IBKRConnectionError\n\n   Bases: :py:obj:`Exception`\n\n\n   Common base class for all non-exit exceptions.\n\n\n",
            "\n",
            t,
            count=1,
        )
        t = re.sub(
            r"\n\.\. py:exception:: IBKRConnectionError\n\n   Bases: :py:obj:`RuntimeError`\n\n\n   Unspecified run-time error.\n\n\n",
            "\n",
            t,
            count=1,
        )
        source[0] = t
    elif docname == "reference/srcPy/ops/index":
        t = source[0]
        t = t.replace(
            "   srcPy.ops.configure_logger\n   srcPy.ops.multi_tier_cache\n   srcPy.ops.get_logger\n",
            "   srcPy.ops.configure_logger\n   srcPy.ops.get_logger\n",
        )
        needle = (
            ".. py:function:: multi_tier_cache(ttl = 60, version = 'v1', "
            "persist_large_objects = False, key_fn = None, redis_client=None, "
            "l2_type = 'memfd', check_l4_on_miss = False)\n"
        )
        if needle in t:
            after = t.split(needle, 1)[1]
            if not after.lstrip().startswith(":no-index:"):
                t = t.replace(needle, needle + "   :no-index:\n")
        source[0] = t
    elif docname == "reference/srcPy/pipeline/core/pipeline_core_base/index":
        t = source[0]
        t = t.replace(
            "   srcPy.pipeline.core.pipeline_core_base.StepRegistry\n   srcPy.pipeline.core.pipeline_core_base.InT\n",
            "   srcPy.pipeline.core.pipeline_core_base.InT\n",
        )
        block = ".. py:data:: StepRegistry\n   :type:  Any\n   :value: Ellipsis\n\n\n"
        if block in t:
            t = t.replace(block, "")
        source[0] = t
    elif docname == "reference/srcPy/pipeline/stages/cleaning/core/base/index":
        t = source[0]
        attr = (
            "Attributes\n----------\n\n.. autoapisummary::\n\n"
            "   srcPy.pipeline.stages.cleaning.core.base.PolarsDataFrame\n\n\n"
        )
        if attr in t:
            t = t.replace(attr, "")
        block = ".. py:data:: PolarsDataFrame\n   :type:  Any\n   :value: Ellipsis\n\n\n"
        if block in t:
            t = t.replace(block, "")
        source[0] = t


def setup(app: Sphinx) -> None:
    sphinx_logging.getLogger("autoapi._mapper").logger.addFilter(
        _SuppressAutoapiPlaceholder()
    )
    app.connect("source-read", _patch_autoapi_duplicate_source)
