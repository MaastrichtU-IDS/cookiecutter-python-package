This page explains how to create a FAIR metrics test API with `{{cookiecutter.package_name}}`.

## 📥 Install the package

Install the package from [PyPI](https://pypi.org/project/{{cookiecutter.package_name}}/){:target="_blank"}:

```bash
pip install {{cookiecutter.package_name}}
```


## 📝 Define the API

Create a `main.py` file to declare the API, you can provide a different folder than `metrics` here, the folder path is relative to where you start the API (the root of the repository):

```python title="main.py"
from {{cookiecutter.module_name}} import Api

api = API()
print(api.hello_world("everyone"))
```
