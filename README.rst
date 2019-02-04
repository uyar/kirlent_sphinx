Copyright (C) 2019 H. Turgut Uyar <uyar@tekir.org>

kirlent_sphinx is a Sphinx extension that is primarily meant to be used with
the Kirlent educational content management system, although it can be used
as a regular Sphinx extension. It consists of the following components:

- An extended ``table`` directive derived from the `cloud_sptheme`_ package.

- A ``slide`` directive and a corresponding, RevealJS-based HTML theme derived
  from the `sphinxjp.themes.revealjs`_ package.

The changes to cloud_sptheme are very small at the moment and the documentation
for the original package should apply. There are some changes to note with
respect to the sphinxjp.themes.revealjs package:

- The ``revealjs`` directive has been renamed to ``slide``.

- The ``rv_note`` directive has been renamed to ``speaker-notes``.

- The ``rv_small`` and ``rv_code`` directives have been removed.

- The HTML theme uses pygments instead of highlight.js.

- The HTML theme uses `bulma`_ for styling. So, for example, you can write
  something like::

    .. slide:: Slide Title

    .. container:: columns

       .. container:: column is-one-third

          - item 1
          - item 2

       .. container:: column is-two-thirds

          - item 3

.. _cloud_sptheme: https://cloud-sptheme.readthedocs.io/en/latest/lib/cloud_sptheme.ext.table_styling.html
.. _sphinxjp.themes.revealjs: https://github.com/tell-k/sphinxjp.themes.revealjs
.. _bulma: https://bulma.io/
