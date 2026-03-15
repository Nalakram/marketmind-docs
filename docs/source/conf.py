from pathlib import Path
import re
import sys


ROOT_DIR = Path(__file__).resolve().parents[2]
DOCS_DIR = Path(__file__).resolve().parents[1]
STUBS_DIR = DOCS_DIR / "stubs"

sys.path.insert(0, str(ROOT_DIR))


project = "MarketMind"
author = "Mark Wuenschel"
copyright = "2025-2026, Mark Wuenschel"


def extract_release(version_text: str) -> str:
    match = re.search(
        r"^##\s*Version\s*([0-9]+\.[0-9]+\.[0-9]+)",
        version_text,
        re.MULTILINE,
    )
    return match.group(1) if match else "0.0.0"


VERSION_PATH = ROOT_DIR / "VERSION.md"
VERSION_TEXT = VERSION_PATH.read_text(encoding="utf-8")
release = extract_release(VERSION_TEXT)
version = ".".join(release.split(".")[:2])

html_title = f"{project} {release} Documentation"
html_short_title = f"{project} Docs"


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
html_extra_path = ["_extra"]
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
    "tensorflow": ("https://www.tensorflow.org/api_docs/python", None),
    "backtrader": ("https://www.backtrader.com/docu/", None),
    "ib_insync": ("https://ib-insync.readthedocs.io/", None),
    "pydantic": ("https://docs.pydantic.dev/latest/", "https://docs.pydantic.dev/latest/objects.inv"),
    "structlog": ("https://www.structlog.org/en/stable/", None),
    "typing_extensions": ("https://typing-extensions.readthedocs.io/en/latest/", None),
    "requests": ("https://requests.readthedocs.io/en/latest/", None),
    "aiohttp": ("https://docs.aiohttp.org/en/stable/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_timeout = 5

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
