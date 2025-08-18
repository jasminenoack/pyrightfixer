import typer

from pyrightfixer.lib.files import get_file_list

app = typer.Typer(help="Example CLI with two commands")


@app.command()
def sandbox(name: str = typer.Argument(".", help="location to run the sandbox")):
    """Show what the command would fix"""
    typer.echo(f"Hello, {name}!")


@app.command()
def fix(name: str = typer.Argument(".", help="Location to fix issues")):
    """Fix the issues in this file"""
    typer.echo(f"Goodbye, {name}!")


@app.command()
def generate(path: str = typer.Argument(help="Path to the generator files")):
    """Generate test files based on the provided path"""
    files = get_file_list(path)
    for file in files:
        typer.echo(f"Processing file: {file}")


if __name__ == "__main__":
    app()
