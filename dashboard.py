#importing
from textual.app import App, ComposeResult 
from textual.widgets import Header, Footer 
from textual.containers import Grid 

#putting all tools i built here
from stopwatch import StopwatchApp  
from cpumonitor import BRAINTracker
from rammonitor import RAMMonitor 
from asciiart import AnimeArt

class DashboardApp(App):
#class for dashboard and css stuff
    CSS_PATH = "dashboard.tcss"
    BINDINGS = [("q", "quit", "Quit Dashboard")]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)

    #to make box layout for every tool
        with Grid(id="master_grid"):
            yield StopwatchApp()
            yield BRAINTracker()
            yield RAMMonitor()
            yield AnimeArt()

        yield Footer()

if __name__ == "__main__":
    app = DashboardApp()
    app.run()        