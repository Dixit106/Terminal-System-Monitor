import psutil
from textual.app import App, ComposeResult 
from textual.widgets import Static 

class RAMMonitor(Static):
    BORDER_TITLE = "RAM Tracker"

    def on_mount(self) -> None:
        #someing like every second tick
        self.update_timer = self.set_interval(1.0, self.update_ram)

    def update_ram(self) -> None:
        #getting ram info using psutil
        ram_percent = psutil.virtual_memory().percent 

        #some maths to convert to gb
        used_gb

        self.update(f"RAM Usage: {ram_percent}%")

class RAMApp(App):
    #css conection to make it look a bit better 
    CSS_PATH = "rammonitor.tcss"

    def compose(self) -> ComposeResult:
        yield RAMMonitor()

if __name__ == "__main__":
    app = RAMApp()
    app.run()                    