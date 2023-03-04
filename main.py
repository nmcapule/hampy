"""."""

from dataclasses import dataclass
from rich.console import Console, ConsoleOptions, RenderResult
from textual import events
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.reactive import reactive
from textual.widgets import Static, TextLog

from game.game import GameView


class MyApp(App):
    CSS = """
    .box {
        border: dashed green;
    }
    .game {
        height: 10;
        width: 20;
    }
    """

    def compose(self) -> ComposeResult:
        yield Horizontal(GameView(classes="box game"), TextLog())

    def on_key(self, event: events.Key) -> None:
        reply = self.query_one(GameView).handle_event(event)
        self.query_one(TextLog).write(reply)


if __name__ == "__main__":
    app = MyApp()
    app.run()
