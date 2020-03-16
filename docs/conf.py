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

# Variables that will be used across multiple documentation pages
# TODO: This is not used at the moment. See a relevant issue:
# https://github.com/zeroguard/zeroguard-api-docs/issues/1
api_version = 'v1'
api_host = 'api.zeroguard.com'

rst_prolog = """
.. |api_version| replace:: {}
.. |api_host| replace:: {}
""".format(
    api_version,
    api_host
)

###############################################################################
# General configuration
###############################################################################
# The master toctree document
master_doc = "index"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'notfound.extension',
    'sphinxcontrib.httpdomain',
    'sphinxcontrib.httpexample',
    'sphinx.ext.intersphinx',
    'sphinxjsondomain',
    'sphinx_rtd_theme'
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
html_show_sphinx = False

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_theme_path = ['.']
html_theme_options = {
    'collapse_navigation': False,
    'navigation_depth': 2
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom JavaScript goes here
html_js_files = [
    'scripts.js'
]

# CSS styles overrides go here
html_css_files = [
    'style.css'
]

# InterSphinx projects mapping
intersphinx_mapping = {
    'python-requests': ('https://requests.readthedocs.io/en/master/', None)
}

# FIXME: Current logo looks horrible so it is disabled. We do need to add
# something prettier at some point though.
#html_logo = 'logo.jpg'

###############################################################################
# Extensions configuration
###############################################################################
# sphinxcontrib-httpexample settings
httpexample_scheme = 'https'
