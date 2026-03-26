#Stopwatch 
from textual.app import App, ComposeResult 
from textual.widgets import Button, Digits, Footer, Header
from textual.containers import HorizontalGroup, VerticalScroll

class TimeDisplay(Digits):
    """A widget to display elapsed time."""

class Stopwatch(HorizontalGroup):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start":
            self.add_class("started")
        elif event.button.id == "stop":
            self.remove_class("started")

    def compose(self) -> ComposeResult:
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")
        yield TimeDisplay("00:00:00.00")

class StopwatchApp(App):
    CSS_PATH = "stopwatch.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield VerticalScroll(Stopwatch(), Stopwatch(), Stopwatch())

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )  

if __name__ == "__main__":
    app = StopwatchApp()
    app.run()     