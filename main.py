"""."""

from textual import events
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import TextLog

from game.game import GameView


class MyApp(App):
    CSS = """
    .box {
        border: dashed green;
    }
    .game {
        height: 14;
        width: 50;
    }
    """

    GAMEVIEW = GameView(classes="box game")

    def compose(self) -> ComposeResult:
        yield Horizontal(self.GAMEVIEW)

    def on_key(self, event: events.Key) -> None:
        """."""
        # reply = self.GAMEVIEW.handle_event(event)
        print(f"oh shit {event}")


if __name__ == "__main__":
    app = MyApp()
    app.run()
