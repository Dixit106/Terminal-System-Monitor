from textual.app import App, ComposeResult 
from textual.widgets import Static 

#creating frames that we can see
FRAME_1 = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⣿⣿⣿⡟⠁⠘⠛⢩⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⣴⣿⣶⣿⡻⠇⠀⠀⠀⠀⠀⠚⢛⡉⠀⠙⠿⢿
⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢹⣿⣿⣿⠦⠤⠀⠀⠀⠀⢰⣿⣿⠿⠀⠀⠀⢠
⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⣈⠙⠛⠛⠓⠂⠀⠀⠀⠀⠀⠀⠀⠠⣤⣀⣴⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣴⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⢹⣿⣿
⣿⣿⣿⣿⠟⠉⠉⠉⠀⠙⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣷⡆⢰⣾⣿⣿
⣿⣿⣿⡿⠀⢰⣶⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⣿⡿⠀⢸⣿⣿⣿
⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢧⠀⠀⠼⣿⣿⣿
⠋⠈⠿⠇⠀⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⣆⠀⠐⠛⠁⣰⣶⣶⣶⣦⣝⣿
⣷⣦⡀⠀⢠⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠻⣤⣶⡖⠈⠋⢹⣿⣿⣿⣿⣿
⣿⣿⣿⣴⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠿⢟⣴⣷⡀⠸⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  """

FRAME_2 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠈⠁⠀⠀⠀⠀⠀⠈⠑⢄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀⣀⣄⢐⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣀⣀⣤⣖⣋⠭⢉⡉⠐⠠⢄⠀⠀⠀⡇⠀⠀⠀⠀
⠀⣠⠔⠂⠉⠀⠀⠀⠀⣀⣀⣤⣀⣀⠀⠉⠑⠂⢵⡀⠀⡄⠀⠀⠀⠀
⢰⡁⠀⢀⢴⠖⢄⣴⣿⣿⡟⢹⠹⣿⣿⢳⣤⣀⠀⠉⠲⣇⠀⠀⠀⠀
⠈⠣⡀⠻⠿⣿⣿⣿⡿⣿⠀⠀⠇⠘⣿⠀⣿⣿⣷⡀⢄⠈⠲⡀⠀⠀
⠀⠀⠈⠂⠤⣡⡟⣿⡇⢘⢒⡂⠀⠀⡺⠯⡙⢻⡿⢷⣼⣆⠀⠈⢂⠀
⠀⠀⠀⠀⠀⠀⠉⠺⣧⢣⣺⡏⡁⠀⢤⣫⠄⢸⣿⡆⣿⠚⠤⠀⣠⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠘⢆⠀⠠⠁⠀⠭⠋⢠⠷⠛⠓⠒⠒⠂⠉⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠤⣀⣀⣤⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠙⠛⠻⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⠺⣋⠀⢀⡤⠖⢟⠜⠉⠒⢂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⡏⠀⢠⠇⠀⠀⠀⢀⠎⠈⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠈⠁⠀⠈⠀⠀⠀⠀⠊⠀⠀⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡰⠂⡲⠀⢀⡀⠀⠀⠀⠀⡠⢲⡈⠲⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⡛⣢⣠⣤⣼⣥⣦⣠⣦⠄⢃⠠⠯⠴⣴⣧⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  """

#making class and stuff
class AnimeArt(Static):

    BORDER_TITLE = "Asciiart"
    def on_mount(self) -> None:
        #something to do with frames
        self.current_frame = 1
        self.update(FRAME_1)

        #To change pic after 0.5s
        self.set_interval(0.5, self.animate)

    def animate(self) -> None:
        #frame 1 will shift to frame 2
        if self.current_frame == 1:
            self.update(FRAME_2)
            self.current_frame = 2
        #otherwise to switch back to frame 1
        else:
            self.update(FRAME_1)
            self.current_frame = 1
#another one of the class and stuff
class GraphicApp(App):
    CSS_PATH = "asciiart.tcss"
    def compose(self) -> ComposeResult:
        yield AnimeArt()
#to start the app in terminal
if __name__ == "__main__":
    app = GraphicApp()
    app.run()                            