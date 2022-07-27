import typer
from {{cookiecutter.package_name}}.api import Api
from {{cookiecutter.package_name}}.version import get_version

cli = typer.Typer()

# Variables to make the prints gorgeous:
BOLD = '\033[1m'
END = '\033[0m'
GREEN = '\033[32m'
# RED = '\033[91m' YELLOW = '\033[33m' CYAN = '\033[36m' PURPLE = '\033[95m' BLUE = '\033[34m'


@cli.command("hello")
def cli_hello(
    name: str = typer.Argument("World", help="Who to greet"),
    output: str = typer.Option(None, help="Path to the output file"),
    verbose: bool = typer.Option(True, help="Display logs")
):
    api = Api()
    print(api.get_hello_world(name))
    if (output):
        if verbose: print(f'Writing to file {BOLD}{GREEN}{output}{END}')
        with open(output, "w") as file:
            file.write(api.get_hello_world(name))



@cli.command("version")
def cli_version():
    print(get_version())


if __name__ == "__main__":
    cli()