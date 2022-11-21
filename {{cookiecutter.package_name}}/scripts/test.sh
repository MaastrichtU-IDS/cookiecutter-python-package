#!/usr/bin/env bash

set -e

pytest --cov=src --cov-report=term-missing:skip-covered ${@}
