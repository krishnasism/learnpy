import typer

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


def main():
    app()
