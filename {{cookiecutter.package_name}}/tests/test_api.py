from {{cookiecutter.module_name}} import Api, VERSION


def test_api():
    """Test the package main function"""
    api = Api()
    assert api.get_hello_world("test") == "Hello test"


def test_version():
    """Test the version is a string."""
    assert isinstance(VERSION, str)