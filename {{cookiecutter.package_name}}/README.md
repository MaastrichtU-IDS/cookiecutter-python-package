<h1 align="center">
  {{cookiecutter.package_name_stylized}}
</h1>

<p align="center">
    <a href="https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/actions/workflows/test.yml">
        <img alt="Tests" src="https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/actions/workflows/test.yml/badge.svg" />
    </a>
    <a href="https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/actions/workflows/publish.yml">
        <img alt="Publish" src="https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/actions/workflows/publish.yml/badge.svg" />
    </a>
    <a href="https://pypi.org/project/{{cookiecutter.package_name}}">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/{{cookiecutter.package_name}}" />
    </a>
    <a href="https://pypi.org/project/{{cookiecutter.package_name}}">
        <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/{{cookiecutter.package_name}}" />
    </a>
    <!-- <a href="https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/blob/main/LICENSE">
        <img alt="PyPI - License" src="https://img.shields.io/pypi/l/{{cookiecutter.package_name}}" />
    </a> -->
    <!-- <a href='https://{{cookiecutter.package_name}}.readthedocs.io/en/latest/?badge=latest'>
        <img src='https://readthedocs.org/projects/{{cookiecutter.package_name}}/badge/?version=latest' alt='Documentation Status' />
    </a> -->
    <!--a href="https://codecov.io/gh/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/branch/main">
        <img src="https://codecov.io/gh/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/branch/main/graph/badge.svg" alt="Codecov status" />
    </a> 
    <a href="https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/blob/main/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg" alt="Contributor Covenant"/>
    </a-->
</p>

{{cookiecutter.short_description}}

## 📥️ Installation

You will need Python >=3.8+ and <3.10

```shell
pip install {{cookiecutter.package_slug}}
```

## 🪄 Usage

### ⌨️ Use as a command-line interface

You can easily use your package from your terminal after installing `{{cookiecutter.package_slug}}` with pip:

```bash
{{cookiecutter.package_slug}}
```

Get a full rundown of the available options with:

```bash
{{cookiecutter.package_slug}} --help
```

### 🐍 Use with python 

This library can also be used directly in python scripts

If your input is tabular data (e.g., csv):

 ```python
import {{cookiecutter.package_name}}

# TODO: add example to use your package
 ```

## 🧑‍💻 Development setup

<details>
  <summary>See developer instructions</summary>

The final section of the README is for if you want to get involved by making a code contribution.

<details><summary>You will need to <a href="https://python-poetry.org/docs">install Poetry</a></summary><br/>

Be careful as poetry sometime uses an unexpected python version by default, you can check for the environment used by poetry in the current folder by running:

```bash
poetry env list
```

You can easily tell `poetry` to use your current version of python for the current folder by running the following command:

```bash
poetry env use $(which python)
```
</details>


### Install

Clone the repository:

```bash
git clone https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}
cd {{cookiecutter.package_slug}}
```

Install the dependencies:

```bash
poetry install
```

### Run

Run the library with the CLI:

```bash
poetry run {{cookiecutter.package_slug}} --help
```

### Test

Run the tests locally:

```bash
poetry run pytest -s
```

### Add a new dependency

You can change the `pyproject.toml` file and run:

```bash
poetry update
```

Or you can do it directly with the CLI (e.g. for `pandas` here):

```bash
poetry add pandas
```

### Generate docs

The documentation is automatically generated from the markdown files in the `docs` folder and python docstring comments, and published by a GitHub Actions workflow.

Start the docs on [http://localhost:8001](http://localhost:8001){:target="_blank"}

```bash
poetry run mkdocs serve -a localhost:8001
```


### Build and publish

Build:

```bash
poetry build
```

Publishing a new release is automatically done by a GitHub Action workflow when a release is created on GitHub:

```bash
poetry publish
```


## 📦️ New release process

The deployment of new releases is done automatically by a GitHub Action workflow when a new release is created on GitHub. To release a new version:

1. Make sure the `PYPI_API_TOKEN` secret has been defined in the GitHub repository (in Settings > Secrets > Actions). You can get an API token from PyPI [here](https://pypi.org/manage/account/).
2. Increment the `version` number in the `pyproject.toml` file in the root folder of the repository.
3. Create a new release on GitHub, which will automatically trigger the publish workflow, and publish the new release to PyPI.

You can also manually trigger the workflow from the Actions tab in your GitHub repository webpage.

</details>