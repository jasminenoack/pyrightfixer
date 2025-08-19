import typer

from pyrightfixer.lib.files import get_file_list
from pyrightfixer.lib.process_errors.processor import Processor
from pyrightfixer.lib.pyright import (
    get_matching_errors,
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
def stepfix(
    path: str = typer.Argument(".", help="Path to fix issues step by step"),
    errors: str = typer.Option(
        "reportDeprecated", "--errors", "-e", help="Comma-separated list of errors to fix"
    ),
):
    """Fix issues step by step in the provided path"""
    typer.echo(f"Step fixing {path} for errors: {errors}...")
    result = run_pyright(path)
    original_total = result.summary.error_count
    typer.echo(f"Original total errors: {original_total}")
    errors_types = errors.split(",")
    all_errors = get_matching_errors(result, errors=errors_types)
    typer.echo(f"Errors to fix: {len(all_errors)}")
    typer.echo("")

    processor = Processor(all_errors)

    while not processor.finished:
        step = processor.next()

        if step and step.proposed_fix:
            result = typer.confirm("Fix this error?")
            if result:
                typer.echo("Applying fix...")
                processor.fix()
            else:
                typer.echo("Skipping this error.")
                processor.skip()
            typer.echo("")
            typer.echo("")
        elif step and not step.proposed_fix:
            typer.echo("")
            typer.echo("")
            continue
        else:
            pass


if __name__ == "__main__":
    app()
