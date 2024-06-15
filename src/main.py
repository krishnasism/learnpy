import typer

from .runner import Runner
from .textual_app import LearnPyApp

app = typer.Typer()


@app.command()
def doc():
    print("Documentation::")


@app.command()
def start():
    """Start learning"""
    learn_py_app = LearnPyApp()
    learn_py_app.run()


@app.command()
def run(script_path: str = "src/exercises/9999_test.py"):
    """Run the script"""
    typer.echo(f"Running {script_path}")
    runner = Runner(script_path)
    runner.run()
    typer.echo(runner.get_stdout())


def main():
    app()
