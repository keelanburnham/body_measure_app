import tkinter as tk
from tkinter import ttk


class InputFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        options = {'padx': 5, 'pady': 5}

        self.weight_label = ttk.Label(self, text='Weight (in lbs):')
        self.weight_label.grid(column=0, row=0, sticky=tk.E, **options)

        self.weight = tk.StringVar()
        self.weight_entry = ttk.Entry(self, textvariable=self.weight)
        self.weight_entry.grid(column=1, row=0, sticky=tk.W, **options)
        self.weight_entry.focus()

        self.save_button = ttk.Button(
            self, text='Save', command=self.save_button_clicked)
        self.save_button.grid(column=1, row=2, sticky=tk.E, **options)

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def save_button_clicked(self):
        if self.controller:
            self.controller.save(self.weight.get())
