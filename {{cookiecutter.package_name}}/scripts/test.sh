#!/usr/bin/env bash

set -e

pytest --cov={{cookiecutter.module_name}} --cov-report=term-missing:skip-covered ${@}
