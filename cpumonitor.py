import psutil
from textual.app import App, ComposeResult
from textual.widgets import Static 

class CPUMonitor(Static):

    def on_mount(self) -> None:
        self.update_timer = self.set_interval(1.0, self.update_cpu)

    def update_cpu(self) -> None:
        cpu_percent = psutil.cpu_percent()

        self.update(f"CPU Usage: {cpu_percent}%")

class CPUApp(App):
    def compose(self) -> ComposeResult:
        yield CPUMonitor()

if __name__ == "__main__":
    app = CPUApp()
    app.run()
                        