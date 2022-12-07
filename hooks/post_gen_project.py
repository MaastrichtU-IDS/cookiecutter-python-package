#!/usr/bin/env python

"""Code to run after generating the project."""

import os
import pathlib
import shutil

PROJECT_DIRECTORY = pathlib.Path(os.path.realpath(os.path.curdir)).resolve()
# PACKAGE = PROJECT_DIRECTORY.joinpath("src", "{{ cookiecutter.module_name }}")
PACKAGE = PROJECT_DIRECTORY.joinpath("{{ cookiecutter.module_name }}")
DOCS = PROJECT_DIRECTORY.joinpath("docs")

if __name__ == '__main__':
    if '{{ cookiecutter.command_line_interface|lower }}' == "false":
        PACKAGE.joinpath("__main__.py").unlink()

    if '{{ cookiecutter.documentation_website|lower }}' == "false":
        PROJECT_DIRECTORY.joinpath("mkdocs.yml").unlink()
        PROJECT_DIRECTORY.joinpath(".github", "workflows", "docs.yml").unlink()
        shutil.rmtree(DOCS)
