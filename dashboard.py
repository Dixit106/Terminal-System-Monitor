#importing
from textual.app import App, ComposeResult 
from textual.widgets import Header, Footer 
from textual.containers import Grid 

#putting all tools i built here
from stopwatch import Stopwatch  
from cpumonitor import BRAINTracker
from rammonitor import RAMMonitor 
from asciiart import AnimeArt

class DashboardApp(App):
#class for dashboard and css stuff
    CSS_PATH = "dashboard.tcss"
    BINDINGS = [("q", "quit", "Quit Dashboard"),
                ("d", "toggle_dark", "Toggle dark mode"),
                ("a", "add_stopwatch", "Add"),
                ("r", "remove_stopwatch", "Remove"),
                ]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)

    #to make box layout for every tool
        with Grid(id="master_grid"):
            yield Stopwatch()
            yield BRAINTracker()
            yield RAMMonitor()
            yield AnimeArt()
        yield Footer()
#
    def action_add_stopwatch(self) -> None:
        new_stopwatch = Stopwatch()
        self.query_one("#timers").mount(new_stopwatch)
        new_stopwatch.scroll_visible()

    def action_remove_stopwatch(self) -> None:
        timers = self.query("Stopwatch")
        if timers:
            timers.last().remove()        

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )  

if __name__ == "__main__":
    app = DashboardApp()
    app.run()        