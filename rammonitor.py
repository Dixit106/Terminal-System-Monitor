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
        ram = psutil.virtual_memory()

        #some maths to convert to gb
        ram_percent = ram.percent
        used_gb = ram.used/(1024 ** 3)
        free_gb = ram.available/(1024 ** 3)

        #.1f will make it show 1 decimal place only like 2.3gb
        #\n to stack them neatly
        self.update(f"RAM Usage: {ram_percent}%\nUsed: {used_gb:.1f} GB\nFree: {free_gb:.1f} GB")

class RAMApp(App):
    #css conection to make it look a bit better 
    CSS_PATH = "rammonitor.tcss"

    def compose(self) -> ComposeResult:
        yield RAMMonitor()

if __name__ == "__main__":
    app = RAMApp()
    app.run()                    