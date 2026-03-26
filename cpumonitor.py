import psutil
from textual.app import App, ComposeResult
from textual.widgets import Static 

class BRAINTracker(Static):
    BORDER_TITLE = "CPU Tracker"

    def on_mount(self) -> None:
        #will kinda update timer for the data
        self.update_timer = self.set_interval(1.0, self.update_cpu)

    def update_cpu(self) -> None:
        #will use psutil import for the hardware data
        cpu_percent = psutil.cpu_percent()
        #ok so finally this thing update the screen we will see
        self.update(f"CPU Usage: {cpu_percent}%")

class CPUApp(App):
    CSS_PATH = "cpumonitor.tcss"

    def compose(self) -> ComposeResult:
        yield BRAINTracker()
        
#for running app as always
if __name__ == "__main__":
    app = CPUApp()
    app.run()
                        