from tkinter import *
from PIL import ImageTk, Image
import os
import python_supabase
from typing import Dict


class GameScreen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Game Screen")
        self.master.resizable(False, False)
        self.createWidgets()
        self.master.after(5000, self.clearScreen)
        self.master.after(5000, self.countdowntimer)

    def createWidgets(self):
        red = '#990000'
        green = '#346C4E'
        redpadx = 152
        greenpadx = redpadx - 2
        codenamex = 89

        def createLabel(text, bg, fg, padx, pady, row, column, columnspan):
            label = Label(text=text, bg=bg, fg=fg, padx=padx, pady=pady)
            label.grid(row=row, column=column, columnspan=columnspan)
            return label

        createLabel('Red Team', 'black', red, redpadx, 10, 0, 0, 2)
        createLabel('Green Team', 'black', green, greenpadx, 10, 0, 2, 2)
        createLabel('Codename', red, 'white', codenamex, 10, 1, 0, 1)
        createLabel('Points', red, 'white', 40, 10, 1, 1, 1)
        createLabel('Codename', green, 'white', codenamex + 4, 10, 1, 2, 1)
        createLabel('Points', green, 'white', 40, 10, 1, 3, 1)
        padloop = (greenpadx+redpadx)+70

        def createblack(text, bg, fg, padx, pady, row, column, columnspan):
            blacklabel = Label(text=text, bg=bg, fg=fg, padx=padx, pady=pady)
            blacklabel.grid(row=row, column=column, columnspan=columnspan)
            return blacklabel

        def createblue(text, bg, fg, padx, pady, row, column, columnspan):
            bluelabel = Label(text=text, bg=bg, fg=fg, padx=padx, pady=pady)
            bluelabel.grid(row=row, column=column,
                           columnspan=columnspan, sticky="ew")
            return bluelabel

        for i in range(10):
            createblack('', 'black', 'black', padloop, 0, i+2, 0, 4)

        for i in range(10):
            createblue('', 'blue', 'blue', (padloop/2)-3, 0, i+12, 0, 2)
            createblue('', 'blue', 'blue', (padloop/2)-3, 0, i+12, 2, 2,)

    def clearScreen(self):
        # Destroy all widgets in the current window
        for widget in self.master.winfo_children():
            widget.destroy()

    def countdowntimer(self, count=10):
        if count >= 0:
            # Get the current directory
            current_directory = os.path.dirname(__file__)
            # Combine the current directory with the directory containing the images and the filename
            image_path = os.path.join(
                current_directory, "countdown_images", f"{count}.tif")
            # Open image
            image = Image.open(image_path)
            # Convert image to PhotoImage
            photo = ImageTk.PhotoImage(image)
            # Create label to display image
            label = Label(image=photo)
            label.image = photo
            label.grid(row=2, column=1)

            # Schedule the next iteration after 1 second
            self.master.after(1000, self.countdowntimer, count-1)
        else:
            # Countdown completed, display createWidgets again
            self.clearScreen()
            self.createWidgets()


class Application(Frame):

    game_started = False

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Team8Photon")
        self.master.resizable(False, False)
        self.frame1 = Frame(master, background='#990000')
        self.frame1.place(x=0, y=0, relwidth=0.5,
                          relheight=1.0, anchor="nw")
        self.frame2 = Frame(master, background='#346C4E')
        self.frame2.place(relx=0.5, y=0, relwidth=0.5,
                          relheight=1.0, anchor="nw")
        self.grid()
        self.createWidgets()
        self.createButton()
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

    def createWidgets(self):
        red = '#990000'
        green = '#346C4E'
        self.red_codename = []
        self.red_id = []
        self.green_codename = []
        self.green_id = []

        Label(text='Red Team', bg=red, fg='white', padx=20,
              pady=20).grid(row=0, column=0, columnspan=2)
        Label(text='Green Team', bg=green, fg='white', padx=20,
              pady=20).grid(row=0, column=2, columnspan=2)
        Label(text='ID', bg=red, fg='white').grid(row=1, column=0)
        Label(text='Codename', bg=red, fg='white').grid(row=1, column=1)
        Label(text='ID', bg=green, fg='white').grid(row=1, column=2)
        Label(text='Codename', bg=green, fg='white').grid(row=1, column=3)

        # Red Team
        for i in range(15):
            entry_red = Entry(bg="white", fg="black",
                              bd=2)
            entry_red.config(justify="right", selectbackground="#D8D8D8", font=('Times 18'), highlightbackground=red,
                             highlightcolor=red)
            entry_red.grid(row=i + 2, column=1)
            entry2_red = Entry(bg="white", fg="black",
                               bd=2)
            entry2_red.config(justify="right", selectbackground="#D8D8D8", font=('Times 18'), highlightbackground=red,
                              highlightcolor=red, width=9)
            entry2_red.grid(row=i + 2, column=0)
            self.red_codename.append(entry_red)
            self.red_id.append(entry2_red)

        # Green Team
        for i in range(15):
            entry_green = Entry(bg="white", fg="black",
                                bd=2)
            entry_green.config(justify="right", selectbackground="#D8D8D8", font=('Times 18'), highlightbackground=green,
                               highlightcolor=green)
            entry_green.grid(row=i + 2, column=3)
            entry2_green = Entry(bg="white", fg="black",
                                 bd=2)
            entry2_green.config(justify="right", selectbackground="#D8D8D8", font=('Times 18'), highlightbackground=green,
                                highlightcolor=green, width=9)
            entry2_green.grid(row=i + 2, column=2)
            self.green_codename.append(entry_green)
            self.green_id.append(entry2_green)

    def createButton(self):
        Button(text="Submit ID", command=self.testing).grid(
            row=18, column=1, columnspan=2)
        Button(text="F5: Start Game", command=self.startGame).grid(
            row=19, column=2, columnspan=2)
        Button(text="F12: Clear Players", command=self.clearPlayers).grid(
            row=19, column=0, columnspan=2)

    def testing(self):
        values = {}
        for codename, id_entry in zip(self.red_codename + self.green_codename, self.red_id + self.green_id):
            name = codename.get()
            id_value = id_entry.get()

            if id_value:
                values[int(id_value)] = name if name else ''

        returned_dict = python_supabase.Database.addData(values)
        for key, value in returned_dict.items():
            for codename, id_entry in zip(self.red_codename + self.green_codename, self.red_id + self.green_id):
                id_value = id_entry.get()
                if id_value and int(id_value) == key:
                    codename.delete(0, END)
                    codename.insert(0, value)

    def clearPlayers(self):
        for entry in self.red_codename:
            entry.delete(0, END)
        for entry in self.red_id:
            entry.delete(0, END)
        for entry in self.green_codename:
            entry.delete(0, END)
        for entry in self.green_id:
            entry.delete(0, END)

    def startGame(self):
        # Clear existing widgets
        for widget in self.master.winfo_children():
            widget.destroy()

        # Create new game screen with 5 rows
        game_screen = GameScreen(self.master)
        game_screen.grid()


root = Tk()
app = Application(root)
root.mainloop()
