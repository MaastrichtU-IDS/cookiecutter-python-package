#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place {{cookiecutter.module_name}} tests --exclude=__init__.py
isort {{cookiecutter.module_name}} tests
pre-commit run --all-files || true

# black {{cookiecutter.module_name}} tests
