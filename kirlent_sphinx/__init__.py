from pathlib import Path

from . import slides, tables


__version__ = "0.1.0"


_template_path = Path(__file__).parent.joinpath("templates")


def get_path():
    """Get the template path.

    :sig: () -> str
    :return: Base path for the templates of this extension.
    """
    return str(_template_path)


def setup(app):
    """Add the directives and themes of this extension to Sphinx.

    :sig: (sphinx.application.Sphinx) -> None
    :param app: Sphinx application to setup.
    """
    slides.setup(app)
    app.add_html_theme("kirlent", str(Path(_template_path, "kirlent")))
    tables.setup(app)
