import asyncio
import os

import aiofiles
from textual.app import ComposeResult
from textual.reactive import reactive
from textual.screen import Screen
from textual.widget import Widget
from textual.widgets import Footer, Header


class Exercise(Widget):
    current_exercise = reactive("exercise")

    def render(self) -> str:
        return f"You are on exercise: {self.current_exercise}"


class ExercisesScreen(Screen):
    BINDINGS = [
        ("d", "toggle_dark", "Toggle Dark Mode"),
        ("e", "exit_screen", "Exit"),
    ]

    problems_map = {
        0: "0000_intro.py",
        1: "0001_print.py",
        2: "0002_import.py",
        3: "0003_arithmetic.py",
        4: "0004_logical.py",
        5: "0005_regex.py",
        6: "0006_algorithm.py",
        7: "0007_test.py",
    }

    def compose(self) -> ComposeResult:
        yield Header()
        yield Exercise()
        yield Footer()

    def exit_screen(self) -> None:
        self.app.pop_screen()

    async def get_current_status(self) -> str:
        async with aiofiles.open(f"{os.path.dirname(os.path.realpath(__file__))}/status") as status_file:
            current_status: str = await status_file.read()
        try:
            current_status_int: int = int(current_status)
        except ValueError:
            # race condition workaround
            current_status_int = 0
        current_problem: str = self.problems_map[int(current_status_int)]
        return current_problem

    async def update_current_status(self):
        while True:
            self.app.query_one(Exercise).current_exercise = await self.get_current_status()
            asyncio.sleep(5)

    def on_mount(self):
        self.run_worker(self.update_current_status)
