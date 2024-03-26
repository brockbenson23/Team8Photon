import json
from dotenv import load_dotenv
from supabase import create_client, Client
from faker import Faker
import faker_commerce
import socket
from tkinter import *
from PIL import ImageTk, Image
import os
import time
import python_supabase

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
        self.red_entries = []
        self.green_entries = []

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
            sv_red = StringVar()
            names_red = StringVar()
            entry_red = Entry(bg="white", fg="black",
                              bd=2, textvariable=sv_red)
            entry_red.config(justify="right", selectbackground="#D8D8D8", font=('Times 18'), highlightbackground=red,
                             highlightcolor=red)
            entry_red.grid(row=i + 2, column=1)
            entry2_red = Entry(bg="white", fg="black",
                               bd=2, textvariable=names_red)
            entry2_red.config(justify="right", selectbackground="#D8D8D8", font=('Times 18'), highlightbackground=red,
                              highlightcolor=red, width=9)
            entry2_red.grid(row=i + 2, column=0)
            sv_red.trace("w", lambda name, index, mode,
                         sv_red=sv_red: python_supabase.Database.getName(python_supabase.Database, sv_red, entry_red, names_red, entry2_red))
            names_red.trace("w", lambda name, index, mode,
                            names_red=names_red: python_supabase.Database.getName(python_supabase.Database, sv_red, entry_red, names_red, entry2_red))
            self.red_entries.append(entry_red)
            self.red_entries.append(entry2_red)

        # Green Team
        for i in range(15):
            sv_green = StringVar()
            names_green = StringVar()
            entry_green = Entry(bg="white", fg="black",
                                bd=2, textvariable=sv_green)
            entry_green.config(justify="right", selectbackground="#D8D8D8", font=('Times 18'), highlightbackground=green,
                               highlightcolor=green)
            entry_green.grid(row=i + 2, column=3)
            entry2_green = Entry(bg="white", fg="black",
                                 bd=2, textvariable=names_green)
            entry2_green.config(justify="right", selectbackground="#D8D8D8", font=('Times 18'), highlightbackground=green,
                                highlightcolor=green, width=9)
            entry2_green.grid(row=i + 2, column=2)
            sv_green.trace("w", lambda name, index, mode,
                           sv_green=sv_green: python_supabase.Database.getName(python_supabase.Database, sv_green, entry_green, names_green, entry2_green))
            names_green.trace("w", lambda name, index, mode,
                              names_green=names_green: python_supabase.Database.getName(python_supabase.Database, sv_green, entry_green, names_green, entry2_green))
            self.green_entries.append(entry_green)
            self.green_entries.append(entry2_green)

    def createButton(self):
        Button(text="Submit ID", command=python_supabase.Database.addData).grid(
            row=18, column=1, columnspan=2)
        Button(text="F5: Start Game", command=self.startGame).grid(
            row=19, column=2, columnspan=2)
        Button(text="F12: Clear Players", command=self.clearPlayers).grid(
            row=19, column=0, columnspan=2)

    def clearPlayers(self):
        for entry in self.red_entries:
            entry.delete(0, END)
        for entry in self.green_entries:
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
