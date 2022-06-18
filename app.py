import tkinter as tk
from controller import Controller
from model import Model
from view import InputFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        window_width = 400
        window_height = 600

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        self.title('Body Measurements')
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        model = Model('123')
        view = InputFrame(self)
        view.grid(padx=10, pady=10, sticky=tk.NSEW)
        controller = Controller(model, view)
        view.set_controller(controller)


if __name__ == "__main__":
    app = App()
    app.mainloop()
