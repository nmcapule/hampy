"""."""
import time

from dataclasses import dataclass
from rich.live import Live
from rich.panel import Panel
from rich.console import Console, ConsoleOptions, RenderResult


@dataclass
class MyView:
    knob: int

    def __rich_console__(
        self, _console: Console, options: ConsoleOptions
    ) -> RenderResult:
        yield "".join(
            [
                f"{(x+y+self.knob)%10}"
                for x in range(options.max_width)
                for y in range(options.max_height)
            ]
        )
        # yield my_table


student = MyView(0)
panel = Panel(student)
panel.height = 10
# panel.width = 20

with Live(panel, refresh_per_second=22):
    for row in range(1200):
        time.sleep(1.0 / 22.0)  # arbitrary delay
        student.knob += 1
