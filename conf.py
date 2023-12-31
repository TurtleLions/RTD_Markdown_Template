# Configuration file for the Sphinx documentation builder.

# -- Project information
github_url = 'https://github.com/TurtleLions'
project = 'PROJECT_NAME'
copyright = 'COPYRIGHT'
author = 'AUTHOR'

release = '0'
version = '0'

# -- General configuration

extensions = [
  'sphinx.ext.duration',
  'sphinx.ext.doctest',
  'sphinx.ext.autodoc',
  'sphinx.ext.autosummary',
  'sphinx.ext.intersphinx',
  'myst_parser',
  'sphinx_rtd_theme'
]

source_suffix = {
  '.rst': 'restructuredtext',
  '.txt': 'markdown',
  '.md': 'markdown',
}

intersphinx_mapping = {
  'python': ('https://docs.python.org/3/', None),
  'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'