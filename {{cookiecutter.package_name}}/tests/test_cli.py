from {{cookiecutter.package_name}}.__main__ import cli
from typer.testing import CliRunner

runner = CliRunner()


def test_cli():
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
