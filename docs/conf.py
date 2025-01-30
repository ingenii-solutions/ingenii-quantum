# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import ingenii_quantum
print(f"Successfully imported ingenii_quantum")

# Add the package's source directory to sys.path
sys.path.insert(0, os.path.abspath("../../"))  # Adjust if needed

# Debugging: Print to confirm Sphinx is using the correct path
print("Sphinx is using:", sys.path[0])

project = 'Ingenii Quantum'
copyright = '2025, Ingenii'
author = 'Ingenii'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

master_doc = "index"

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', "../exercises.py", "../custom.py"]

extensions = [
    "sphinx.ext.autodoc",    # Extracts docstrings
    "sphinx.ext.napoleon",   # Supports Google/NumPy-style docstrings
    "sphinx.ext.viewcode",   # Adds source code links
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_logo = "_static/logo.png"
html_favicon = "_static/favicon.ico"
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

