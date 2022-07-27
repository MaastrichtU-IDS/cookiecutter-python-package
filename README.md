# Cookiecutter Snekpack

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) for making new Python repositories.

This template is different from [@audreyfeldroy](https://github.com/audreyfeldroy)'s
[cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) because it uses the source
layout and has lots of code quality assurance checks built in. If you're looking for something similar but not quite
like this, try her package or see her [list of alternatives](https://cookiecutter-pypackage.readthedocs.io/en/latest/readme.html#similar-cookiecutter-templates).


## 🛠️ Getting Started

1. Install `cookiecutter` with:

```shell
pip install cookiecutter
```

2. Run `cookiecutter` with:

```shell
cookiecutter https://github.com/MaastrichtU-IDS/cookiecutter-python-package
```

3. Enter the requested information, then win! Remember, package names should only have letters, numbers, and underscores.

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
- A good base `.gitignore` generated from [gitignore.io](https://gitignore.io).
- A pre-formatted README with badges
- A pre-formatted LICENSE file with the MIT License (you can change this to whatever you want, though)
- A pre-formatted CONTRIBUTING guide
- A pre-formatted `CITATION.cff` file
