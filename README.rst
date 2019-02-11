Copyright (C) 2019 H. Turgut Uyar <uyar@tekir.org>

kirlent_sphinx is a Sphinx extension that is primarily meant to be used with
the `Kırlent`_ educational content management system, although it can be used
as a regular Sphinx extension.

Features
--------

kirlent_sphinx provides the following components:

- An extended ``table`` directive derived from the `Cloud Sphinx Theme`_
  project.

- A ``slide`` directive and a corresponding HTML theme based on `RevealJS`_,
  derived from the `sphinxjp.themes.revealjs`_ project.

Getting started
---------------

You can install kirlent_sphinx with pip::

  pip install kirlent_sphinx

To enable it in your project, make the following changes in ``conf.py``:

- Add ``kirlent_sphinx`` to extensions::

    extensions = ["kirlent_sphinx"]

- Set ``kirlent`` as the theme::

    html_theme = "kirlent"

- Disable index generation::

    html_use_index = False

Usage
-----

For the extended ``table`` directive, consult the documentation
of the `table_styling`_ extension of the `Cloud Sphinx Theme`_ project.

The ``slide`` and ``speaker-notes`` directives are derived from the
``revealjs`` and ``rv_note`` directives of the `sphinxjp.themes.revealjs`_
project. The ``rv_small`` and ``rv_code`` directives of that project have been
removed.

The Kırlent HTML theme uses pygments for code highlighting instead of
highlight.js which is used by the original theme. In addition, it uses
the `Bulma`_ framework for styling. So, Bulma classes are available
by default::

  .. slide:: Slide Title

     .. container:: columns

        .. container:: column is-one-third

           - item 1
           - item 2

        .. container:: column is-two-thirds

           - item 3

.. _Kırlent: https://gitlab.com/tekir/kirlent/
.. _Cloud Sphinx Theme: https://cloud-sptheme.readthedocs.io/en/latest/
.. _table_styling: https://cloud-sptheme.readthedocs.io/en/latest/lib/cloud_sptheme.ext.table_styling.html
.. _sphinxjp.themes.revealjs: https://github.com/tell-k/sphinxjp.themes.revealjs
.. _RevealJS: https://revealjs.com/
.. _Bulma: https://bulma.io/
