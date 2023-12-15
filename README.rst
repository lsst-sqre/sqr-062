.. image:: https://img.shields.io/badge/sqr--062-lsst.io-brightgreen.svg
   :target: https://sqr-062.lsst.io/
.. image:: https://github.com/lsst-sqre/sqr-062/workflows/CI/badge.svg
   :target: https://github.com/lsst-sqre/sqr-062/actions/

#####################################################################################################
The Times Square service for publishing parameterized Jupyter Notebooks in the Rubin Science platform
#####################################################################################################

SQR-062
=======

The Times Square service publishes Jupyter Notebooks as webpages within the Rubin Science Platform (though outside JupyterLab). Authors of notebooks can parameterize text and code within the notebook's source. Viewers of the notebook can select values for these parameters to view a notebook rendered on-demand in conjunction with the Noteburst notebook service. Times Square is intended to be used for publishing live dashboards and reports of observatory operations and data processing activities. This technical note covers the concept and design of Times Square.


**Links:**

- Publication URL: https://sqr-062.lsst.io/
- Alternative editions: https://sqr-062.lsst.io/v
- GitHub repository: https://github.com/lsst-sqre/sqr-062
- Build system: https://github.com/lsst-sqre/sqr-062/actions/

Build this technical note
=========================

You can clone this repository and build the technote locally if your system has Python 3.11 or later:

.. code-block:: bash

   git clone https://github.com/lsst-sqre/sqr-062
   cd sqr-062
   make init
   make html

Repeat the ``make html`` command to rebuild the technote after making changes.
If you need to delete any intermediate files for a clean build, run ``make clean``.

The built technote is located at ``_build/html/index.html``.

Publishing changes to the web
=============================

This technote is published to https://sqr-062.lsst.io/ whenever you push changes to the ``main`` branch on GitHub.
When you push changes to a another branch, a preview of the technote is published to https://sqr-062.lsst.io/v.

Editing this technical note
===========================

The main content of this technote is in ``index.rst`` (a reStructuredText file).
Metadata and configuration is in the ``technote.toml`` file.
For guidance on creating content and information about specifying metadata and configuration, see the Documenteer documentation: https://documenteer.lsst.io/technotes.
