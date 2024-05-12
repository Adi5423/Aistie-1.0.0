import tkinter as tk
from tkinter.commondialog import Dialog

class MessageWithButtons(Dialog):
    "A message box with custom buttons"

    def body(self, master):
        label = tk.Label(master, text=self.options["message"])
        label.pack(padx=10, pady=10)
        self.buttons = []
        for (text, code) in self.options["buttons"]:
            button = tk.Button(master, text=text, command=self.ok, default=self.options["default"] == code)
            button.pack(side="left", padx=5, pady=5)
            self.buttons.append(button)
        return label

    def apply(self):
        # Set the result to the value of the default button
        self.result = self.options["default"]
        # Enable the default button
        self.buttons[self.options["default"]].config(relief="raised")
        # Disable the other buttons
        for i in range(len(self.buttons)):
            if i != self.options["default"]:
                self.buttons[i].config(relief="flat")