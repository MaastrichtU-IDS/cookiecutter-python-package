# 🍪🐍 Cookiecutter for modern Python packages

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for making new Python package repositories using modern tools for developments.

Tired of needing to install and configure 42 different packages for linting? Tired of having 15 config files at the root of the repository? With this template all configurations are stored in the `pyproject.toml` using the [new standard project metadata](https://peps.python.org/pep-0621/), and `ruff` is used to perform a super-fast linting.

We use [`hatch`](https://hatch.pypa.io/latest/) for the overall project management and build backend. Hatch is a bit like poetry, it helps to tie together your python project and easily run scripts in virtual environments. But it is the solution supported by PyPA (the Python Packaging Authority), and relies on existing well established packages under the hood (like `pip` and `venv`), instead of re-implementing everything.


## 🛠️ Getting Started

1. Install `cookiecutter` with:

```bash
pipx install cookiecutter
```

2. Run `cookiecutter` with:

```bash
cookiecutter https://github.com/MaastrichtU-IDS/cookiecutter-python-package
```

3. Enter the requested information, remember, package names should only have letters, numbers, and dashes.

4. If you're working under version control, copy the repository into your folder tracked under git, commit the files, and push to your remote.

## 💪 Features

Your new python package will have the following:

- Standard `src/` layout
- Declarative setup with `pyproject.toml`
- Super fast linting and formatting with [`ruff`](https://github.com/astral-sh/ruff) and `black` 
- Reproducible tests with `pytest`
- A command line interface with `typer`
- Documentation build with [`mkdocs`](https://squidfunk.github.io/mkdocs-material)
- A `py.typed` file so other packages can use your type hints
- Automated running of tests on each push with GitHub Actions
- A good and readable base `.gitignore` for python projects
- A pre-formatted README with badges
- A pre-formatted LICENSE file with the MIT License (you can change this to whatever you want, though)
- A pre-formatted CONTRIBUTING guide
- A pre-formatted `CITATION.cff` file

If you're looking for something similar but not quite like this see this [list of alternatives templates](https://cookiecutter-pypackage.readthedocs.io/en/latest/readme.html#similar-cookiecutter-templates).
