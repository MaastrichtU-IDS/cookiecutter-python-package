<div align="center">

# {{cookiecutter.package_name_stylized}}

[![PyPI - Version](https://img.shields.io/pypi/v/{{cookiecutter.package_name}}.svg?logo=pypi&label=PyPI&logoColor=silver)](https://pypi.org/project/{{cookiecutter.package_name}}/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{cookiecutter.package_name}}.svg?logo=python&label=Python&logoColor=silver)](https://pypi.org/project/{{cookiecutter.package_name}}/)
[![license](https://img.shields.io/pypi/l/{{cookiecutter.package_name}}.svg?color=%2334D058)](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_name}}/blob/main/LICENSE.txt){% if cookiecutter.black_formatting|lower != "false" %}
[![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black){% endif %}

[![Test package](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_name}}/actions/workflows/test.yml/badge.svg)](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_name}}/actions/workflows/test.yml)
[![Publish package](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_name}}/actions/workflows/publish.yml/badge.svg)](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_name}}/actions/workflows/publish.yml)

</div>

{{cookiecutter.short_description}}

## 📦️ Installation

This package requires Python >=3.7, simply install it with:

```shell
pip install {{cookiecutter.package_name}}
```

## 🪄 Usage
{% if cookiecutter.command_line_interface|lower != "false" %}
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
git clone https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_name}}
cd {{cookiecutter.package_name}}
```
### 🐣 Install dependencies

Install [Hatch](https://hatch.pypa.io), this will automatically handle virtual environments and make sure all dependencies are installed when you run a script in the project:

```bash
pip install --upgrade hatch
```

Install the dependencies in a local virtual environment:

```bash
hatch -v env create
```

### ☑️ Run tests

Make sure the existing tests still work by running ``pytest``. Note that any pull requests to the fairworkflows repository on github will automatically trigger running of the test suite;

```bash
hatch run test
```

To display all logs when debugging:

```bash
hatch run test -s
```

### 🧹 Code formatting

The code will be automatically formatted when you commit your changes using `pre-commit`. But you can also run the script to format the code yourself:

```
hatch run fmt
```

Check the code for errors, and if it is in accordance with the PEP8 style guide, by running `flake8` and `mypy`:

```
hatch run check
```
{% if cookiecutter.documentation_website|lower != "false" %}
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

### 🏷️ New release process

The deployment of new releases is done automatically by a GitHub Action workflow when a new release is created on GitHub. To release a new version:

1. Make sure the `PYPI_TOKEN` secret has been defined in the GitHub repository (in Settings > Secrets > Actions). You can get an API token from PyPI at [pypi.org/manage/account](https://pypi.org/manage/account).
2. Increment the `version` number in the `pyproject.toml` file in the root folder of the repository.
3. Create a new release on GitHub, which will automatically trigger the publish workflow, and publish the new release to PyPI.

You can also manually trigger the workflow from the Actions tab in your GitHub repository webpage.
