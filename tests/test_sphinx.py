from pytest import fixture

import subprocess
from pathlib import Path
from shutil import rmtree

from pkg_resources import get_distribution

from kirlent_sphinx import __version__


SOURCE = "/dev/shm/kirlent_sphinx"

CONF_PY_CONTENT = """
extensions = ["kirlent_sphinx"]
html_theme = "kirlent_revealjs"
html_use_index = False
master_doc = "index"
"""

SLIDE_CONTENT_1 = """
.. slide:: Slide title

   - item 1
"""


TABLE_CONTENT_1 = """
.. slide:: Slide title

   .. table::
      :widths: 1 2

      +---+---+
      | a | b |
      +---+---+
"""


@fixture(scope="session", autouse=True)
def setup_sphinx():
    """A skeleton Sphinx project."""
    Path(SOURCE).mkdir(parents=True, exist_ok=True)
    conf_py = Path(SOURCE, "conf.py")
    conf_py.write_text(CONF_PY_CONTENT)
    yield
    rmtree(SOURCE)


def test_version():
    assert get_distribution("kirlent_sphinx").version == __version__


def test_slide_directive_should_be_available():
    Path(SOURCE, "index.rst").write_text(SLIDE_CONTENT_1)
    subprocess.call(["sphinx-build", "-b", "html", SOURCE, SOURCE + "/_build"])
    assert Path(SOURCE, "_build", "index.html").exists()


def test_table_directive_should_be_available():
    Path(SOURCE, "index.rst").write_text(TABLE_CONTENT_1)
    subprocess.call(["sphinx-build", "-b", "html", SOURCE, SOURCE + "/_build"])
    assert Path(SOURCE, "_build", "index.html").exists()
