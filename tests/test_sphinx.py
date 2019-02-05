from pkg_resources import get_distribution

from kirlent_sphinx import __version__


def test_version():
    assert get_distribution("kirlent_sphinx").version == __version__
