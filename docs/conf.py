"""Configuration file for Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the offical Sphinx documentation:

    https://www.sphinx-doc.org/en/master/usage/configuration.html
"""
# pylint: disable=C0103,C0413,E0401,W0622
from datetime import datetime

###############################################################################
# Project information
###############################################################################
project = 'Zeroguard Recon API'
release = '0.0.1-dev.1'

author = 'ZeroGuard'
copyright = '%s ZeroGuard Ltd' % datetime.now().year

###############################################################################
# General configuration
###############################################################################
# The master toctree document
master_doc = "index"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store'
]

###############################################################################
# Options for HTML output
###############################################################################
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'
html_theme_path = ['.']
html_theme_options = {
    'description': (
        'ZeroGuard Recon threat intelligence platform public API documentation'
    ),
    'github_user': 'zeroguard',
    'github_repo': 'zeroguard-api-docs',
    'github_banner': False,
    'github_button': True,
    'logo': 'logo.jpg',
    'show_powered_by': False,
    'show_relbars': True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_show_sphinx = False

###############################################################################
# Extensions configuration
###############################################################################
