import tkinter as tk


class EntryPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="", color="grey", *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.fg_color = self["fg"]
        self.focus_out()

        self.bind("<FocusIn>", self.focus_in)
        self.bind("<FocusOut>", self.focus_out)

    def focus_in(self, *args):
        if self["fg"] == self.placeholder_color:
            self.delete(0, "end")
            self["fg"] = self.fg_color

    def focus_out(self, *args):
        if self.get() == "":
            self["fg"] = self.placeholder_color
            self.insert(0, self.placeholder)
