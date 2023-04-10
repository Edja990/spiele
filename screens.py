import tkinter
import select
root = tkinter.Tk()
x = 0

class Screens:

    def __init__(self):
        self.gamelist = ["pingpong", "Doom"]
        self.gamedict = {"pingpong": self.open_pingpong, "Doom": self.open_doom}
        self.tk = root
        self.tk.attributes('-fullscreen', True)  # This just maximizes it so we can see the window. It's nothing to do with fullscreen.
        self.frame = tkinter.Frame(self.tk)
        self.frame.pack()
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"
    def button(self):
        for i in range(len(self.gamelist)):
            self.label1 = tkinter.Label(root, text=self.gamelist[i], bg="orange")
            self.label1.pack()
            self.button_pingpong = tkinter.Button(root, text=self.gamelist[i], command= self.gamedict[self.gamelist[i]])
            self.button_pingpong.pack()

    def open_pingpong(self):
        self.select.sel_pingpong = select.sel_pingpong()
    def open_doom(self):
        self.select.sel_doom = select.sel_doom()

    def start(self):
        global firsttime
        self.button()
        self.w = Screens()
        self.w.tk.mainloop()

