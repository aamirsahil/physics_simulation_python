import PySimpleGUI as sg
import os

class GUI:
    def __init__(self, width=100, height=50, title="Hello World!!") -> None:
        self.width = width
        self.height = height
        self.title = title
        self.layout = None
        self.window = None
    def start(self):
        self.setLayout()
        # create window
        self.window = sg.Window(self.title, self.layout, margins=(self.width, self.height))
    def setLayout(self):
        first_list_column = [
            [
                sg.Text("Image Folder"),
                sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
                sg.FolderBrowse()
            ],
            [
                sg.Listbox(
                    values=[], enable_events=True, size=(40,20), key="-FILE LIST-"
                )
            ],
        ]
        image_viewer_column = [
            [sg.Text("Choose an image from list on left:")],
            [sg.Text(size=(40,1), key="-TOUT-")],
            [sg.Image(key="-IMAGE-")],
        ]
        # define layout
        self.layout = [
            [
                sg.Column(first_list_column),
                sg.VSeparator(),
                sg.Column(image_viewer_column)
            ]
        ]
    def close(self):
        self.window.close()
    def read(self):
        event, values = self.window.read()
        if event == "-FOLDER-":
            event = "Folder Selected"
        elif event == "-FILE LIST-":
            event = "File Selected"
        elif event==sg.WIN_CLOSED:
            event = "Quit"
        return event, values
    def listFiles(self, values={}):
        folder = values["-FOLDER-"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []
        fnames = [
            f for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        self.window["-FILE LIST-"].update(fnames)
    def showImage(self, values):
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            self.window["-TOUT-"].update(filename)
            self.window["-IMAGE-"].update(filename=filename)
        except:
            pass
def main():
    gui = GUI(width=100, height=50, title="Image viewer")
    gui.start()
    while True:
        event, values = gui.read()
        if event=="Folder Selected":
            print(event, values)
            gui.listFiles(values)
        elif event=="File Selected":
            print(event, values)
            gui.showImage(values)
        elif event=="Quit":
            print(event, values)
            break
    gui.close()
if __name__=="__main__":
    main()