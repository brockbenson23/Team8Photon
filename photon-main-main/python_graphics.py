# Import required libraries
# from tkinter import *
# from PIL import ImageTk, Image as im

# Import required libraries
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = Tk()
win.title("Team8Photon")
win.geometry("700x700")

path = "logo.jpg"

img = ImageTk.PhotoImage(Image.open(path))
original_image = Image.open(path)
resized_image = original_image.resize((700, 700))

img = ImageTk.PhotoImage(resized_image)

label = Label(win, image=img)
label.grid()


win.after(3000, win.destroy)
win.mainloop()

red = '#990000'
green = '#346C4E'


class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Team8Photon")
        self.master.resizable(False, False)
        self.frame1 = Frame(master, background=red)
        self.frame1.place(x=0, y=0, relwidth=0.5,
                          relheight=1.0, anchor="nw")
        self.frame2 = Frame(master, background=green)
        self.frame2.place(relx=0.5, y=0, relwidth=0.5,
                          relheight=1.0, anchor="nw")
        self.grid()
        self.createWidgets()
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

    def createWidgets(self):
        self.Label = Label(text='Red Team', bg=red, fg='white')
        self.Label.configure(padx=20, pady=20)
        self.Label.grid(row=0, column=0, columnspan=2)
        self.Label = Label(text='Green Team', bg=green, fg='white')
        self.Label.configure(padx=20, pady=20)
        self.Label.grid(row=0, column=2, columnspan=2)
        self.Label = Label(text='ID', bg=red, fg='white')
        self.Label.grid(row=1, column=0)
        self.Label = Label(text='Codename', bg=red, fg='white')
        self.Label.grid(row=1, column=1)
        self.Label = Label(text='ID', bg=green, fg='white')
        self.Label.grid(row=1, column=2)
        self.Label = Label(text='Codename', bg=green, fg='white')
        self.Label.grid(row=1, column=3)

        for i in range(15):
            self.entry = Entry(bg="white", fg="black", bd=2)
            self.entry.config(justify="right", selectbackground="#D8D8D8", font=('Times 26'), highlightbackground=red,
                              highlightcolor=red)

            self.entry.grid(row=i+2, column=1)
        for i in range(15):
            self.entry = Entry(bg="white", fg="black", bd=2)
            self.entry.config(justify="right", selectbackground="#D8D8D8", font=('Times 26'), highlightbackground=green,
                              highlightcolor=green)
            self.entry.grid(row=i+2, column=3)
        for i in range(15):
            self.entry = Entry(bg="white", fg="black", bd=2)
            self.entry.config(justify="right", selectbackground="#D8D8D8", font=('Times 26'), highlightbackground=red,
                              highlightcolor=red, width=9)
            self.entry.grid(row=i+2, column=0)
        for i in range(15):
            self.entry = Entry(bg="white", fg="black", bd=2)
            self.entry.config(justify="right", selectbackground="#D8D8D8", font=('Times 26'), highlightbackground=green,
                              highlightcolor=green, width=9)
            self.entry.grid(row=i+2, column=2)

        def getName(id: str,) -> str:
            f = open("player.sql", "r")
            index = 0
            for line in f:
                word = f.readline()
                if f"VALUES ({id}," in word:
                    code = word[10:]
                    index += 1
                else:
                    break
            f.close()
            f = open("player.sql", "a")
            f.write(f"\nVALUES ({id}, \"newCodeName\");")

        self.button = Button(text="Submit ID", command=getName("12345"))
        self.button.grid(row=18, column=1, columnspan=2)
        # l1 = Label(win, text = "First:")
        # l2 = Label(win, text = "Second:")

        # l1.grid(row = 0, column = 0, sticky = W, pady = 2)
        # l2.grid(row = 1, column = 0, sticky = W, pady = 2)

        # e1 = Entry(master)
        # e2 = Entry(master)
        # e1.grid(row  = 0, column = 1, pady = 2)
        # e2.grid(row  = 1, column = 1, pady = 2)
root = Tk()
app = Application(root)
root.mainloop()