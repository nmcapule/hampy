import dataclasses
from textual import events
from textual.geometry import Size
from textual.reactive import reactive
from textual.widgets import Static


@dataclasses.dataclass
class Coord:
    col: int
    row: int


class GameRenderable:
    _size = None
    buffer: list[list[str]] = []

    def __init__(self, size=None):
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, val: Size):
        if (
            not self._size
            or self._size.width != val.width
            or self._size.height != val.height
        ):
            self._size = Size(width=val.width, height=val.height)
            self.buffer = [
                [" " for col in range(self._size.width)]
                for row in range(self._size.height)
            ]

    def render(self):
        return "\n".join(["".join(col) for col in self.buffer])

    def draw(self, coord: Coord, val: str):
        if coord.col >= self._size.width:
            pass
        if coord.row >= self._size.height:
            pass
        self.buffer[coord.row][coord.col] = val


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
        self.update(self.game.render())

    # def handle_event(self, event: events.Event):
    #     if isinstance(event, events.Key):
    #         self.game.draw(self._character, "-")
    #         match event.key:
    #             case "left":
    #                 self._character.col -= 1
    #             case "right":
    #                 self._character.col += 1
    #             case "up":
    #                 self._character.row -= 1
    #             case "down":
    #                 self._character.row += 1
    #         self.game.draw(self._character, "[blue]X[/]")
    #     return event
