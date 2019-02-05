from pytest import fixture

import subprocess
from pathlib import Path
from shutil import rmtree

from pkg_resources import get_distribution

from kirlent_sphinx import __version__


SOURCE = "/dev/shm/kirlent_sphinx"


@fixture(scope="session", autouse=True)
def setup_sphinx():
    """A skeleton Sphinx project."""
    Path(SOURCE).mkdir(parents=True, exist_ok=True)
    conf_py = Path(SOURCE, "conf.py")
    conf = """extensions=["kirlent_sphinx"]\nhtml_theme="kirlent"\nhtml_use_index=False\nmaster_doc="index"\n"""
    conf_py.write_text(conf)
    yield
    rmtree(SOURCE)


def test_version():
    assert get_distribution("kirlent_sphinx").version == __version__


def test_slide_directive_should_be_available():
    content = ".. slide:: Slide Title\n\n   - item 1\n"
    Path(SOURCE, "index.rst").write_text(content)
    subprocess.call(["sphinx-build", "-b", "html", SOURCE, SOURCE + "/_build"])
    assert Path(SOURCE, "_build", "index.html").exists()


def test_table_directive_should_be_available():
    content = ".. slide:: Slide Title\n\n   .. table::      :widths: 1\n\n      +---+\n      | a |\n      +---+\n"
    Path(SOURCE, "index.rst").write_text(content)
    subprocess.call(["sphinx-build", "-b", "html", SOURCE, SOURCE + "/_build"])
    assert Path(SOURCE, "_build", "index.html").exists()
