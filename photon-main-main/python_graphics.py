# Import required libraries
# from tkinter import *
# from PIL import ImageTk, Image as im

# Import required libraries
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = Tk()
win.title("Team8Photon")
win.geometry("300x300")

path = "logo.jpg"

img = ImageTk.PhotoImage(Image.open(path))
original_image = Image.open(path)
resized_image = original_image.resize((300, 300))

img = ImageTk.PhotoImage(resized_image)

label = Label(win, image=img)
label.grid()


win.after(3000, win.destroy)
win.mainloop()


class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Team8Photon")
        self.frame1 = Frame(master, background='#990000')
        self.frame1.place(x=0, y=0, relwidth=0.5,
                          relheight=1.0, anchor="nw")
        self.frame2 = Frame(master, background="#346C4E",)
        self.frame2.place(relx=0.5, y=0, relwidth=0.5,
                          relheight=1.0, anchor="nw")
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        for i in range(15):
            self.entry = Entry(bg="white", fg="black", bd=0)
            self.entry.config(highlightbackground="#990000",
                              highlightcolor="#990000")
            self.entry.grid(row=i, column=0)
        for i in range(15):
            self.entry = Entry(bg="white", fg="black", bd=0)
            self.entry.config(highlightbackground="#346C4E",
                              highlightcolor="#346C4E")
            self.entry.grid(row=i, column=1)


root = Tk()
app = Application(root)
root.mainloop()
