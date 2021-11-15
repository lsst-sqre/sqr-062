:tocdepth: 1

.. Please do not modify tocdepth; will be fixed when a new Sphinx theme is shipped.

.. sectnum::

Abstract
========

The Times Square service publishes Jupyter Notebooks as webpages within the Rubin Science Platform (though outside JupyterLab).
Authors of notebooks can parameterize text and code within the notebook's source.
Viewers of the notebook can select values for these parameters to view a notebook rendered on-demand in conjunction with the Noteburst notebook service.
Times Square is intended to be used for publishing live dashboards and reports of observatory operations and data processing activities.
This technical note covers the concept and design of Times Square.

The key functionality of Times Square
=====================================

This section summarizes the key features of Times Square that affect the user experience:

- |TS| maintains a database of Jupyter Notebooks.
  These notebooks can be stored as ``ipynb`` files in a GitHub repository along with a sidecar YAML file that provides metadata (e.g. title and description) along with the schema for the parameterized variables.

- Jupyter Notebooks are *parameterized* with Jinja_ templating syntax.
  Both text and code cells can be templated so that either the prose or the computed results of the notebook are generated dynamically.

- Each notebook is published to the web as its own path: ``/<root>/<notebook slug>``.
  When a user visits a page's URL, |TS| returns an HTML rendering of the executed notebook.
  By requesting the bare path, the user sees a notebook rendered from default parameters.
  However, the user can also add a query string to the URL to see the notebook rendered with those parameters, e.g. ``/<root>/<notebook slug>?myvar=42&greeting=hello+world``.

- For users in a web browser, |TS| provides a wrapper around the HTML-rendered notebook.
  This wrapper provides a form interface for selecting notebook parameters, along with basic metadata and navigation elements.
  The interface also provides a link for downloading the ipynb file for further editing beyond the scope of the parameterization.

- At its root URL, ``/<root>/``, |TS| displays an index of available notebooks.

.. Add content here.
.. Do not include the document title (it's automatically added from metadata.yaml).

.. .. rubric:: References

.. Make in-text citations with: :cite:`bibkey`.

.. .. bibliography:: local.bib lsstbib/books.bib lsstbib/lsst.bib lsstbib/lsst-dm.bib lsstbib/refs.bib lsstbib/refs_ads.bib
..    :style: lsst_aa
