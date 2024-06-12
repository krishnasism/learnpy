from textual import on
from textual.app import ComposeResult
from textual.containers import Container, Horizontal
from textual.screen import Screen
from textual.widgets import Button, Label


class WelcomeScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Label("Welcome to learnpy. Get started?", id="question", classes="question")
        yield Container(
            Horizontal(
                Button("Yes", id="yes", variant="primary"),
                Button("No", id="no", variant="error"),
                classes="buttons",
            ),
            id="dialog",
        )

    @on(Button.Pressed, "#yes")
    def yes_pressed(self) -> None:
        self.app.push_screen("exercises_screen")

    @on(Button.Pressed, "#no")
    def no_pressed(self) -> None:
        exit(0)
