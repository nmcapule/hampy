import dataclasses
from rich.console import Console, ConsoleOptions, RenderResult
from textual import events
from textual.geometry import Size
from textual.reactive import reactive
from textual.widgets import Static


@dataclasses.dataclass
class Coord:
    col: int
    row: int


class GameRenderable:
    size = None
    buffer: list[list[str]] = []

    def __init__(self, size=None):
        self.size = size

    def __rich_console__(
        self, _console: Console, options: ConsoleOptions
    ) -> RenderResult:
        if (
            self.size.width != options.max_width
            or self.size.height != options.max_height
        ):
            self.size = Size(width=options.max_width, height=options.max_height)
            self.buffer = [
                ["_" for col in range(self.size.width)]
                for row in range(self.size.height)
            ]
        yield "".join(["".join(col) for col in self.buffer])

    def draw(self, coord: Coord, s: str):
        if coord.col >= self.size.width:
            pass
        if coord.row >= self.size.height:
            pass
        self.buffer[coord.row][coord.col] = s


class GameView(Static):
    tick = reactive(0)
    game = GameRenderable()

    _character = Coord(0, 0)

    def on_mount(self) -> None:
        self.set_interval(1.0 / 60.0, self.update_tick)

    def update_tick(self):
        self.tick += 1

    def watch_tick(self):
        self.game.size = self.size
        self.update(self.game)

    def handle_event(self, event: events.Event):
        if isinstance(event, events.Key):
            self.game.draw(self._character, "-")
            match event.key:
                case "left":
                    self._character.col -= 1
                case "right":
                    self._character.col += 1
                case "up":
                    self._character.row -= 1
                case "down":
                    self._character.row += 1
            self.game.draw(self._character, "X")
        return event
