import typer

from pyrightfixer.lib.files import get_file_list
from pyrightfixer.lib.pyright_run import (
    print_meta_info,
    pyright_error_diagnostics,
    pyright_file_diagnostics,
    run_pyright,
)

app = typer.Typer(help="Example CLI with two commands")


@app.command()
def scan(
    path: str = typer.Argument(".", help="Path to scan for issues"),
    show_file_diagnostics: bool = typer.Option(
        False, "--show-file-diagnostics", "-s", help="Show file diagnostics"
    ),
    show_error_diagnostics: bool = typer.Option(
        False, "--show-error-diagnostics", "-g", help="Show general diagnostics"
    ),
    detailed: bool = typer.Option(
        False, "--vv", "-d", help="Show detailed diagnostics"
    ),
):
    """Scan the provided path for issues"""
    typer.echo(f"Scanning {path}...")
    result = run_pyright(path)
    print_meta_info(result)
    if show_error_diagnostics:
        pyright_error_diagnostics(result, detailed)
    if show_file_diagnostics:
        pyright_file_diagnostics(result, detailed)


@app.command()
def sandbox(name: str = typer.Argument(".", help="location to run the sandbox")):
    """Show what the command would fix"""
    typer.echo(f"Running sandbox on {name}...")
    result = run_pyright(name)
    typer.echo("")
    pyright_error_diagnostics(result)
    typer.echo("")
    pyright_file_diagnostics(result, detailed=False)
    typer.echo("")
    pyright_file_diagnostics(result, detailed=True)


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
