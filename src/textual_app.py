from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

from .components.exercises_screen import ExercisesScreen
from .components.welcome_screen import WelcomeScreen


class LearnPyApp(App):
    """Learn Python"""

    TITLE = "learnpy"
    SUB_TITLE = "Learn Python with practice"
    CSS_PATH = "resources/styles/learnpy.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle Dark Mode"),
        ("e", "exit_app", "Exit"),
    ]

    def on_mount(self) -> None:
        self.install_screen(WelcomeScreen(), name="welcome_screen")
        self.install_screen(ExercisesScreen(), name="exercises_screen")

    def compose(self) -> ComposeResult:
        yield Header()
        yield WelcomeScreen()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """Toggle dark mode"""
        self.dark = not self.dark

    def action_exit_app(self) -> None:
        self.exit(return_code=0)
