[![Version](https://img.shields.io/pypi/v/{{cookiecutter.package_slug}})](https://pypi.org/project/{{cookiecutter.package_slug}}) [![Python versions](https://img.shields.io/pypi/pyversions/{{cookiecutter.package_slug}})](https://pypi.org/project/{{cookiecutter.package_slug}}) [![Pull requests welcome](https://img.shields.io/badge/pull%20requests-welcome-brightgreen)](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/fork)

[![Run tests](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/actions/workflows/tests.yml/badge.svg)](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/actions/workflows/tests.yml) [![CodeQL](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/actions/workflows/codeql-analysis.yml) [![Coverage](https://sonarcloud.io/api/project_badges/measure?project={{cookiecutter.github_organization_name}}_{{cookiecutter.package_slug}}&metric=coverage)](https://sonarcloud.io/dashboard?id={{cookiecutter.github_organization_name}}_{{cookiecutter.package_slug}})

[![Publish to PyPI](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/actions/workflows/publish.yml/badge.svg)](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/actions/workflows/publish.yml) [![Publish docs](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/actions/workflows/publish-docs.yml/badge.svg)](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/actions/workflows/publish-docs.yml)

### 📥 Install for development

Clone the repository and install the dependencies locally for development:

```bash
git clone https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}
cd {{cookiecutter.package_slug}}
pip install -e .
```

??? bug "If you are facing issues, use a virtual environment to avoid conflicts"

    Create the virtual environment folder in your workspace:
    
    ```bash
    python3 -m venv .venv
    ```
    
    Activate the virtual environment:
    
    ```bash
    source .venv/bin/activate
    ```


### ✅ Run the tests

[![Run tests](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/actions/workflows/tests.yml/badge.svg)](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/actions/workflows/tests.yml) [![Coverage](https://sonarcloud.io/api/project_badges/measure?project={{cookiecutter.github_organization_name}}_{{cookiecutter.package_slug}}&metric=coverage)](https://sonarcloud.io/dashboard?id={{cookiecutter.github_organization_name}}_{{cookiecutter.package_slug}})

Tests are automatically run by a GitHub Actions workflow when new code is pushed to the GitHub repository. The subject URLs to test and their expected score are retrieved from the `test_test` attribute for each metric test.

??? success "Install `pytest` for testing"

    ```bash
    pip install pytest
    ```

??? note "If not already done, define the 2 files required to run the tests"

    It will test all cases defined in your FAIR metrics tests `test_test` attributes:
    
    ```python title="tests/conftest.py"
    def pytest_addoption(parser):
        parser.addoption("--metric", action="store", default=None)
    ```
    
    and:
    
    ```python title="tests/test_metrics.py"
    import pytest
    from fastapi.testclient import TestClient
    from main import app
    
    endpoint = TestClient(app)
    
    def test_api(pytestconfig):
        app.run_tests(endpoint, pytestconfig.getoption('metric'))
    ```

Run the tests locally (from the root folder):

```bash
pytest -s
```

Run the tests only for a specific metric test:

```bash
pytest -s --metric a1-metadata-protocol
```

### 📖 Generate docs

[![Publish docs](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/actions/workflows/publish-docs.yml/badge.svg)](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/actions/workflows/publish-docs.yml)

The documentation (this website) is automatically generated from the markdown files in the `docs` folder and python docstring comments, and published by a GitHub Actions workflow.

??? abstract "Install the dependencies to generate and serve the documentation locally"

    ```bash
    pip install -r docs/requirements.txt
    ```

Start the docs on [http://localhost:8001](http://localhost:8001){:target="_blank"}

```bash
mkdocs serve -a localhost:8001
```

### 🏷️ Publish a new release

[![Publish to PyPI](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/actions/workflows/publish.yml/badge.svg)](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.package_slug}}/actions/workflows/publish.yml)

1. Increment the version in `setup.py`
2. Push to GitHub
3. Create a new release on GitHub
4. A GitHub Action workflow will automatically publish the new version to PyPI
