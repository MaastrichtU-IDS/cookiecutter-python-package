#!/usr/bin/env bash

set -e

isort {{cookiecutter.module_name}} tests --check-only
flake8 {{cookiecutter.module_name}} tests
mypy {{cookiecutter.module_name}}
# black {{cookiecutter.module_name}} tests --check
