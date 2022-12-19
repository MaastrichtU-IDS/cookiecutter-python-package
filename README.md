# 🍪🐍 Cookiecutter for Python package

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for making new Python package repositories.

This template uses the `hatch` build backend, `mkdocs` for the documentation website, and `typer` for the optional CLI. If you're looking for something similar but not quite
like this see this [list of alternatives templates](https://cookiecutter-pypackage.readthedocs.io/en/latest/readme.html#similar-cookiecutter-templates).


## 🛠️ Getting Started

1. Install `cookiecutter` with:

```shell
pip install cookiecutter
```

2. Run `cookiecutter` with:

```shell
cookiecutter https://github.com/MaastrichtU-IDS/cookiecutter-python-package
```

3. Enter the requested information, then win! Remember, package names should only have letters, numbers, and dashes.

4. If you're working under version control, copy the repository into your folder tracked under git, commit the files, and push to your remote.

## 💪 Features

Your new python package will have the following:

- Standard `src/` layout
- Declarative setup with `pyproject.toml`
- Reproducible tests with `pytest`
- A command line interface with `typer`
- A vanity CLI via python entrypoints
<!-- - Version management with `bumpversion` -->
- Documentation build with `mkdocs`
- A `py.typed` file so other packages can use your type hints
- Automated running of tests on each push with GitHub Actions
- A good and readable base `.gitignore` for python projects
- A pre-formatted README with badges
- A pre-formatted LICENSE file with the MIT License (you can change this to whatever you want, though)
- A pre-formatted CONTRIBUTING guide
- A pre-formatted `CITATION.cff` file
