#!/usr/bin/env python

"""Code to run after generating the project."""

import os
import pathlib
import shutil

PROJECT_DIRECTORY = pathlib.Path(os.path.realpath(os.path.curdir)).resolve()
# PACKAGE = PROJECT_DIRECTORY.joinpath("src", "{{ cookiecutter.module_name }}")
PACKAGE = PROJECT_DIRECTORY.joinpath("src", "{{ cookiecutter.module_name }}")
DOCS = PROJECT_DIRECTORY.joinpath("docs")
PACKAGE_NAME = "{{ cookiecutter.package_name }}"

BOLD = "\033[1m"
END = "\033[0m"
RED = "\033[91m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

if __name__ == '__main__':
    if '{{ cookiecutter.init_git|lower }}' != "no":
        os.system(f"cd {PROJECT_DIRECTORY} && git init")

    if '{{ cookiecutter.command_line_interface|lower }}' == "no":
        PACKAGE.joinpath("__main__.py").unlink()
        PROJECT_DIRECTORY.joinpath("tests", "test_cli.py").unlink()

    if '{{ cookiecutter.documentation_website|lower }}' == "no":
        PROJECT_DIRECTORY.joinpath("mkdocs.yml").unlink()
        shutil.rmtree(DOCS)

    if '{{ cookiecutter.enable_pre_commit|lower }}' == "no":
        PROJECT_DIRECTORY.joinpath(".pre-commit-config.yaml").unlink()

    print(
        f"✅ Your project has been successfully generated in {BOLD}{PACKAGE_NAME}{END}.\n"
        f"📂 Enter it with {BOLD}cd {PACKAGE_NAME}{END}\n"
        "✍️  To do:\n"
        f"- Check the citation generated in {BOLD}CITATION.cff{END} is correct\n"
        f"- Check the documentation in the {BOLD}README.md{END} to learn how to work with the code generated\n"
        f"- Add dependencies in {BOLD}pyproject.toml{END}\n"
        f"- Update the tests in the {BOLD}test/{END} folder"
    )