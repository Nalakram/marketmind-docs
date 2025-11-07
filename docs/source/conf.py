# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# Configuration file for the Sphinx documentation builder.

import os
import sys
import re

# -- Path setup --------------------------------------------------------------

# Add your project directory to sys.path, so autodoc can find your code (if using API docs)
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------

project = 'MarketMind'
author = 'Mark Wuenschel'

# 1) Locate VERSION.md in your repo root
version_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "VERSION.md")
)

# 2) Read & extract the semver (X.Y.Z) after "## Version"
release = "0.0.0"
with open(version_path, encoding="utf-8") as f:
    content = f.read()
    m = re.search(
        r"^##\s*Version\s*([0-9]+\.[0-9]+\.[0-9]+)",
        content,
        re.MULTILINE,
    )
    if m:
        release = m.group(1)  # e.g. "1.11.0"

# 3) Split into major & minor.patch
major, minor_patch = release.split(".", 1)  # -> "1", "11.0"

# 4) Tell Sphinx about your version info
version = release   # (you could also do ".".join(release.split(".")[:2]) if you want "1.11")
release = release   # full

# 5) Override the HTML <title> and the header banner
html_title = f"{project} v{major} {minor_patch} Project Docs"
html_short_title = html_title

copyright = '2025, Mark Wuenschel'

# -- General configuration ---------------------------------------------------
extensions = [
    # --- Content Parsing and Source Formats ---
    # 'myst_nb',                         # Full Jupyter Notebook (.ipynb) support (execution and parsing of notebooks)
    'myst_parser',                     # Support for MyST Markdown (.md files) including Sphinx directives inside Markdown

    # --- API and Autodoc Generation ---
    'sphinx.ext.autodoc',              # Core: Automatically document Python modules/classes/functions from docstrings
    'sphinx.ext.napoleon',             # Support for Google-style and NumPy-style docstrings in autodoc
    'sphinx_autodoc_typehints',        # Format Python type hints automatically in signatures and docstrings
    'sphinxcontrib.autodoc_pydantic',  # Extended autodoc support for Pydantic models (fields, validators, config)
    'autoapi.extension',               # Automatically build API documentation from source files (Python and other languages)
    'sphinx.ext.autosummary',          # Auto-generate summary tables for modules/classes/functions for quick navigation

    # --- Diagrams and Visuals ---
    'sphinxcontrib.mermaid',           # Render Mermaid.js diagrams (flowcharts, sequence diagrams, etc.)
    'sphinx.ext.graphviz',             # Embed raw Graphviz DOT diagrams directly into docs (needs Graphviz installed)

    # --- Math Support ---
    'sphinx.ext.mathjax',              # Render LaTeX-style math equations using MathJax in HTML output

    # --- Usability and UX Enhancements ---
    'sphinx_copybutton',               # Adds a copy button to code blocks (for easier code snippet copying)
    'sphinx.ext.viewcode',             # Adds hyperlinks to highlighted Python source code for documented objects
    'sphinx.ext.todo',                 # Support for .. todo:: directives; auto-generates a TODO list page
    'sphinx_design',                   # Provides modern responsive UI components like tabs, cards, and grids (great for HTML output)

    # --- External References / Cross-linking ---
    'sphinx.ext.intersphinx',          # Enables links to other projects' documentation (e.g., Python stdlib, NumPy, etc.)
]

# Enable MyST extensions for Markdown

myst_parser_add_suffix = False

myst_enable_extensions = [
    "colon_fence",        # ::: fenced directives
    "deflist",            # Definition lists
    "html_admonition",    # HTML-style admonitions
    "html_image",         # Raw HTML images
    "smartquotes",        # Smart typography (curly quotes)
    "replacements",       # Common text replacements (e.g., (C) → ©)
    "linkify",            # Auto-link URLs
    "attrs_inline",       # Inline attribute lists (for styling)
    "substitution",       # Text substitutions / variables
    "tasklist",           # GitHub-style task lists ([x], [ ])
    "dollarmath",         # Inline and block LaTeX math with $ and $$
    "attrs_inline",       # For inline formatting
    "attrs_block",        # For heading IDs like {#id}
]

myst_heading_anchors = 3 # Enable automatic anchor links for headings (supports `{#id}` syntax in Markdown)

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# The master toctree document.
# master_doc = 'index'  # Because your docs/ folder is symlinked

# List of patterns, relative to source directory, that match files/directories to ignore when looking for source files.
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '**.ipynb_checkpoints',
    '.venv',
    '.tox',
    '.pytest_cache',
    '*.egg-info',
]

# -- Options for HTML output -------------------------------------------------

html_theme = 'furo'  # Clean, minimal, responsive theme with light/dark mode support

# Where Sphinx will look for custom static files (e.g., CSS, images)
html_static_path = ['_static']
html_extra_path  = ['_extra']            # add this for raw HTML
html_css_files = ["custom.css"]

# Customize Furo color palette or other theme options
html_theme_options = {
    "navigation_with_keys": True,
}

# -- autodoc_pydantic configuration ---------------------------------------------------
autodoc_pydantic_model_show_json = True                # Include JSON schema for models
autodoc_pydantic_model_show_config_summary = True      # Show Pydantic config attributes
autodoc_pydantic_model_show_field_summary = True       # Show fields in summary tables
autodoc_pydantic_field_show_constraints = True         # Show type constraints (like max_length, etc)
autodoc_pydantic_model_member_order = "bysource"       # Order fields/methods by source order
autodoc_pydantic_model_show_field_type = True          # Show each field's type annotation in the field summary
autodoc_pydantic_model_show_validator_summary = True   # Include a summary table of model validators
autodoc_pydantic_model_show_validator_regex = True     # Show regex patterns for any fields with regex validators
autodoc_pydantic_settings_show_config_member = True    # Include the Pydantic Config class as a documented member


# -- sphinxcontrib-mermaid ---------------------------------------------------

mermaid_output_format = "svg"  # Output Mermaid diagrams as SVG for crisp scaling and RTD compatibility

# -- AutoAPI config -----------------------------------------------

autoapi_type = 'python'             # Tell AutoAPI we are documenting Python source code

autoapi_add_toctree_entry = True    # Automatically add AutoAPI-generated modules to the Sphinx TOC tree

# Source directories for AutoAPI to scan (absolute path recommended)
autoapi_dirs = [os.path.abspath(os.path.join(__file__, '..', '..', 'stubs'))]
autoapi_python_use_stub_files = True

# Exclude test files and directories from API docs
autoapi_ignore = [
    '*/tests/*',                    # Ignore any test modules
    '*/__init__.py',                # (Optional) Skip empty __init__ modules unless you want them
]

# Control which elements AutoAPI documents
autoapi_options = [
    "members",                      # Document all members (functions, classes, etc.)
    "undoc-members",                # Include members with no docstring (helps catch missing docs)
    "show-inheritance",             # Show class inheritance diagrams or base classes
    "show-module-summary",          # Show short summary for each module at the top
    "special-members",              # (Optional) Include Python special methods like __init__, __str__, etc.
    "imported-members",             # (Optional) Include imported names from other modules (can be noisy)
    "show-module-members",
]

# (Optional but Recommended) Control file layout for generated docs
autoapi_keep_files = True           # Keeps the generated .rst/.md files for inspection/debugging (great during early setup)

# (Optional) Where the generated API docs will appear in your final doc hierarchy
autoapi_root = "reference"          # Means AutoAPI-generated pages will live under /reference/ in the built docs


# -- Intersphinx Mapping ------------------------------------------------------

intersphinx_mapping = {
    # Core Python and Standard Library
    'python': ('https://docs.python.org/3', None),

    # Data Science / Machine Learning Libraries
    'numpy': ('https://numpy.org/doc/stable/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/', None),
    'sklearn': ('https://scikit-learn.org/stable/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'statsmodels': ('https://www.statsmodels.org/stable/', None),
    'joblib': ('https://joblib.readthedocs.io/en/latest/', None),

    # Deep Learning Frameworks
    'torch': ('https://pytorch.org/docs/stable/', './_static/inventories/objects.inv'),
    'tensorflow': ('https://www.tensorflow.org/api_docs/python', None),  # ⚠️ No intersphinx inventory available

    # Finance / Trading Libraries
    'backtrader': ('https://www.backtrader.com/docu/', None),             # ⚠️ No intersphinx inventory available
    'ib_insync': ('https://ib-insync.readthedocs.io/', None),

    # Supporting and Utility Libraries
    'pydantic': ('https://docs.pydantic.dev/latest/', 'https://docs.pydantic.dev/latest/objects.inv'),
    'structlog': ('https://www.structlog.org/en/stable/', None),
    'typing_extensions': ('https://typing-extensions.readthedocs.io/en/latest/', None),
    'requests': ('https://requests.readthedocs.io/en/latest/', None),
    'aiohttp': ('https://docs.aiohttp.org/en/stable/', None),

    # Optional: Sphinx internal documentation
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

# Timeout setting for fetching intersphinx inventories (helps prevent build hangs if external sites are down)
intersphinx_timeout = 5  # seconds

# -- Math Support -------------------------------------------------------------

mathjax_config = {
    "tex2jax": {
        "inlineMath": [['$', '$'], ['\\(', '\\)']],  # Allow $...$ and \( ... \) for inline math
        "displayMath": [['$$', '$$'], ['\\[', '\\]']],  # Allow $$...$$ and \[...\] for block math
    }
}

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"  # Use latest MathJax v3 CDN

# -- Autodoc Options ----------------------------------------------------------

autodoc_default_options = {
    "members": True,               # Document all members
    "undoc-members": True,         # Include undocumented members
    "show-inheritance": True,      # Show base classes for classes
    "inherited-members": True,     # Document inherited members
    "special-members": "__init__", # Document __init__ functions
}

autodoc_typehints = "description"  # Render type hints as part of the function/method description (instead of in signature)

autodoc_typehints_format = "short"  # Use short type names (like `int` instead of `builtins.int`)

# -- Autosummary Options ------------------------------------------------------

autosummary_generate = True  # Automatically generate _autosummary/*.rst files during build

autosummary_imported_members = False  # (Optional) Don't include externally imported 

# -- TODO Extension Options ---------------------------------------------------

todo_include_todos = True  # If True, include TODOs in the output HTML build (can toggle off for releases)

# -- Misc options ------------------------------------------------------------

root_path = os.path.abspath("../..")
version_path = os.path.join(root_path, "VERSION.md")
changelog_path = os.path.abspath("CHANGELOG.md")  # inside docs/source/

with open(version_path, encoding="utf-8") as f:
    version_md = f.read()

# Find all version entries
entries = re.findall(r"(## Version [0-9]+\.[0-9]+\.[0-9]+.*?)(?=^## Version |\Z)", version_md, re.DOTALL | re.MULTILINE)

# Compose changelog content
changelog_content = "# Changelog\n\nThis is auto-generated from [VERSION.md on GitHub](https://github.com/MindForgeLabs/MarketMind/blob/main/VERSION.md.\n\n"
for entry in entries:
    changelog_content += entry.strip() + "\n\n---\n\n"

# Strip final trailing --- *before* writing
changelog_content = changelog_content.strip()
if changelog_content.endswith('---'):
    changelog_content = changelog_content[:-3].strip()

# Write to CHANGELOG.md
with open(changelog_path, "w", encoding="utf-8") as f:
    f.write(changelog_content)