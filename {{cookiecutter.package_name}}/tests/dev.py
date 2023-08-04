import logging

from {{cookiecutter.module_name}} import Api, parse_settings

# Script to use to try the package in development

settings = parse_settings("tests/data/settings.yml")

# Add code to test the lib in development
api = Api(settings)
print(api.hello_world("test"))
