<div align="center">

# {{cookiecutter.package_name_stylized}}

[![PyPI - Version](https://img.shields.io/pypi/v/{{cookiecutter.package_name}}.svg?logo=pypi&label=PyPI&logoColor=silver)](https://pypi.org/project/{{cookiecutter.package_name}}/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{cookiecutter.package_name}}.svg?logo=python&label=Python&logoColor=silver)](https://pypi.org/project/{{cookiecutter.package_name}}/)
[![license](https://img.shields.io/pypi/l/{{cookiecutter.package_name}}.svg?color=%2334D058)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}/blob/main/LICENSE.txt)

[![Test package](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}/actions/workflows/test.yml/badge.svg)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}/actions/workflows/test.yml)
[![Publish package](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}/actions/workflows/publish.yml/badge.svg)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}/actions/workflows/publish.yml)

[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg){ loading=lazy .off-glb }](https://github.com/pypa/hatch) [![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json){ loading=lazy .off-glb }](https://github.com/astral-sh/ruff) [![code style - Black](https://img.shields.io/badge/code%20style-black-000000.svg){ loading=lazy .off-glb }](https://github.com/psf/black) [![types - Mypy](https://img.shields.io/badge/types-Mypy-blue.svg){ loading=lazy .off-glb }](https://github.com/python/mypy)

</div>

{{cookiecutter.short_description}}

## 📦️ Installation

This package requires Python >=3.8, simply install it with:

```bash
pip install {{cookiecutter.package_name}}
```

You can also install directly from the git repository:

```bash
pip install git+https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}.git
```

## 🪄 Usage
{% if cookiecutter.command_line_interface|lower != "no" %}
### ⌨️ Use as a command-line interface

You can easily use your package from your terminal after installing `{{cookiecutter.package_name}}` with pip:

```bash
{{cookiecutter.package_name}}
```

Get a full rundown of the available options with:

```bash
{{cookiecutter.package_name}} --help
```

### 🐍 Use with python

{% endif %} Use this package in python scripts:

 ```python
import {{cookiecutter.module_name}}

# TODO: add example to use your package
 ```

## 🧑‍💻 Development setup

The final section of the README is for if you want to run the package in development, and get involved by making a code contribution.


### 📥️ Clone

Clone the repository:

```bash
git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}
cd {{cookiecutter.package_name}}
```
### 🐣 Install dependencies

Install [Hatch](https://hatch.pypa.io), this will automatically handle virtual environments and make sure all dependencies are installed when you run a script in the project:

```bash
pipx install hatch
```

### ☑️ Run tests

Make sure the existing tests still work by running the test suite and linting checks. Note that any pull requests to the fairworkflows repository on github will automatically trigger running of the test suite;

```bash
hatch run test
```

To display all logs when debugging:

```bash
hatch run test -s
```

You can also run the tests on multiple python versions:

```bash
hatch run all:test
```

{% if cookiecutter.documentation_website|lower != "no" %}
### 📖 Generate documentation

The documentation is automatically generated from the markdown files in the `docs` folder and python docstring comments, and published by a GitHub Actions workflow.

Start the docs on [http://localhost:8001](http://localhost:8001){:target="_blank"}

```bash
hatch run docs
```
{% endif %}
### ♻️ Reset the environment

In case you are facing issues with dependencies not updating properly you can easily reset the virtual environment with:

```bash
hatch env prune
```

Manually trigger installing the dependencies in a local virtual environment:

```bash
hatch -v env create
```

### 🏷️ New release process

The deployment of new releases is done automatically by a GitHub Action workflow when a new release is created on GitHub. To release a new version:

1. Make sure the `PYPI_TOKEN` secret has been defined in the GitHub repository (in Settings > Secrets > Actions). You can get an API token from PyPI at [pypi.org/manage/account](https://pypi.org/manage/account).
2. Increment the `version` number in the `pyproject.toml` file in the root folder of the repository.
3. Create a new release on GitHub, which will automatically trigger the publish workflow, and publish the new release to PyPI.

You can also manually trigger the workflow from the Actions tab in your GitHub repository webpage.
