"""Sphinx configuration."""
project = "Pyinfuse"
author = "Nanosystems Lab"
copyright = "2024, Nanosystems Lab"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
