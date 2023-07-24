# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'pytorch_sphinx_theme'
html_theme_path = [pytorch_sphinx_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# yapf: disable
html_theme_options = {
    'menu': [
        {
            'name': 'GitHub',
            'url': 'https://github.com/L1183325308/opencompass'
        },
    ],
    # Specify the language of shared menu
    'menu_lang': 'en',
    # Disable the default edit on GitHub
    'default_edit_on_github': False,
}

# yapf: enable
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

html_static_path = ['_static']
html_css_files = [
    'https://cdn.datatables.net/v/bs4/dt-1.12.1/datatables.min.css',
    'css/readthedocs.css'
]
html_js_files = [
    'https://cdn.datatables.net/v/bs4/dt-1.12.1/datatables.min.js',
    'js/custom.js'
]
# html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
