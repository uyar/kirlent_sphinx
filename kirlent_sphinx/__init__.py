from pathlib import Path

from . import directives


__version__ = "0.1.0"


_template_path = Path(__file__).parent.joinpath("templates")


def get_path():
    """Get the template path.

    :sig: () -> str
    """
    return str(_template_path)


def setup(app):
    """Add the directives and theme to Sphinx.

    :sig: (sphinx.application.Sphinx) -> None
    :param app: Sphinx application to setup.
    """
    directives.setup(app)
    app.add_html_theme("kirlent", str(Path(_template_path, "kirlent")))
