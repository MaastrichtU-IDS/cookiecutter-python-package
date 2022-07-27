from {{cookiecutter.package_name}} import Api
from {{cookiecutter.package_name}}.version import get_version


def test_api():
    """Test the package main function"""
    api = Api()
    assert api.get_hello_world("test") == "Hello test"


def test_version():
    """Test the version is a string."""
    version = get_version()
    assert isinstance(version, str)