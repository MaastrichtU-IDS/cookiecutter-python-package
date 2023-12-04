from {{cookiecutter.module_name}} import Api, __version__, parse_settings


def test_api():
    """Test the package main function"""
    api = Api()
    assert api.hello_world("test") == "[0] Hello test [1] Hello test "


def test_parse_settings():
    """Test parsing YAML settings file"""
    settings = parse_settings("tests/resources/settings.yml")
    assert settings.greet == "everyone"


def test_version():
    """Test the version is a string."""
    assert isinstance(__version__, str)
