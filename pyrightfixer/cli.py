import typer

app = typer.Typer(help="Example CLI with two commands")

@app.command()
def sandbox(name: str = typer.Argument(".", help="location to run the sandbox")):
    """Show what the command would fix"""
    typer.echo(f"Hello, {name}!")

@app.command()
def fix(name: str = typer.Argument(".", help="Location to fix issues")):
    """Fix the issues in this file"""
    typer.echo(f"Goodbye, {name}!")

if __name__ == "__main__":
    app()