import time
import pygame
import random
from typing import Dict
from python_udpclient import broadcastID
import python_gamefuncs
import python_supabase
from tkinter import *
from PIL import ImageTk, Image
import os
import math
print('after math')
print('after gamefuncs')

# comment this out its so useless but don't delete clifford needs it
# import test


class GameScreen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Game Screen")
        self.master.resizable(False, False)
        self.countdowntimer()
        self.pickSound()
        self.game_timer_label = None

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

        self.game_timer_label = Label(self.master, text="Game Timer: 00:00", font=(
            "Arial", 16), bg='black', fg='white')
        self.game_timer_label.grid(row=1, column=0, columnspan=4, sticky="ew")

        createLabel('Red Team', 'black', red, redpadx, 10, 0, 0, 2)
        createLabel('Green Team', 'black', green, greenpadx, 10, 0, 2, 2)
        createLabel('Codename', red, 'white', codenamex,
                    10, 2, 0, 1)         # Adjusted row
        createLabel('Points', red, 'white', 40, 10, 2, 1,
                    1)                   # Adjusted row
        createLabel('Codename', green, 'white', codenamex + 4,
                    10, 2, 2, 1)    # Adjusted row and column
        createLabel('Points', green, 'white', 40, 10, 2,
                    3, 1)                 # Adjusted row
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

        for i in range(10):  # display players & points here
            createblack('red codename', 'black',
                        'black', padloop/2, 0, i+2, 0, 2)
            createblack('points ', 'black', 'black', padloop/2, 0, i+2, 2, 4)

        for i in range(10):  # display game actions here
            createblue('', 'blue', 'blue', (padloop/2)-3, 0, i+12, 0, 2)
            createblue('', 'blue', 'blue', (padloop/2)-3, 0, i+12, 2, 2,)

    def clearScreen(self):
        # Destroy all widgets in the current window
        for widget in self.master.winfo_children():
            widget.destroy()

    def pickSound(self):
        # Play the countdown sound
        randomInt = random.randint(1, 8)
        print(randomInt)
        match randomInt:
            case 1:
                track = "photon_tracks\Track01.mp3"
            case 2:
                track = "photon_tracks\Track02.mp3"
            case 3:
                track = "photon_tracks\Track03.mp3"
            case 4:
                track = "photon_tracks\Track04.mp3"
            case 5:
                track = "photon_tracks\Track05.mp3"
            case 6:
                track = "photon_tracks\Track06.mp3"
            case 7:
                track = "photon_tracks\Track07.mp3"
            case 8:
                track = "photon_tracks\Track08.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(track)
        pygame.mixer.music.play()

    def countdowntimer(self, count=5):

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
            self.game_timer_label = Label(self.master, text="Game Timer: 00:00", font=(
                "Arial", 16), bg="black", fg="white")
            self.game_timer_label.grid(
                row=1, column=0, columnspan=4, sticky="ew")
            broadcastID('202')
            # Start the game timer
            self.gameTimer(0)

    def gameTimer(self, count):
        if count <= 360:
            minutes = count // 60
            seconds = count % 60
            timer_text = f"Game Timer: {minutes:02d}:{seconds:02d}"
            self.game_timer_label.config(text=timer_text)
            self.master.after(1000, self.gameTimer, count+1)
        else:
            black_strip = Label(self.master, bg="black")
            black_strip.grid(row=24, column=0, columnspan=4, sticky="ew")
            end_button = Button(self.master, text="Game Over",
                                command=self.handleGameEnd)
            end_button.grid(row=24, column=0, columnspan=4)

    def handleGameEnd(self):
        # Clear the current screen
        self.clearScreen()
        # Get the parent frame (Application frame)
        self.application_instance.createWidgets()
        self.application_instance.createButton()


class Application(Frame):

    game_started = False
    # declaring teams
    RED = python_gamefuncs.Team()
    GREEN = python_gamefuncs.Team()
    python_supabase.Database.clearEquipmentIds()

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
        self.List = {}

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
            entry_red_id = Entry(bg="white", fg="black", bd=2, state=NORMAL)
            entry_red_id.config(justify="right", selectbackground="#D8D8D8", font=('Times 18'), highlightbackground=red,
                                highlightcolor=red, width=9)
            entry_red_id.grid(row=i + 2, column=0)
            entry_red_codename = Entry(
                bg="white", fg="black", bd=2, state=DISABLED)
            entry_red_codename.config(justify="right", selectbackground="#D8D8D8", font=('Times 18'), highlightbackground=red,
                                      highlightcolor=red)
            entry_red_codename.grid(row=i + 2, column=1)
            self.red_codename.append(entry_red_codename)
            self.red_id.append(entry_red_id)
            self.List[entry_red_id] = entry_red_codename

        # Green Team
        for i in range(15):
            entry_green_id = Entry(
                bg="white", fg="black", bd=2, state=NORMAL)
            entry_green_id.config(justify="right", selectbackground="#D8D8D8", font=('Times 18'), highlightbackground=green,
                                  highlightcolor=green, width=9)
            entry_green_id.grid(row=i + 2, column=2)
            entry_green_codename = Entry(
                bg="white", fg="black", bd=2, state=DISABLED)
            entry_green_codename.config(justify="right", selectbackground="#D8D8D8", font=('Times 18'), highlightbackground=green,
                                        highlightcolor=green)
            entry_green_codename.grid(row=i + 2, column=3)
            self.green_codename.append(entry_green_codename)
            self.green_id.append(entry_green_id)
            self.List[entry_green_id] = entry_green_codename

    def createButton(self):
        Button(text="Submit ID", command=self.addPlayer).grid(
            row=18, column=1, columnspan=2)
        Button(text="F5: Start Game", command=self.startGame).grid(
            row=19, column=2, columnspan=2)
        Button(text="F12: Clear Players", command=self.clearPlayers).grid(
            row=19, column=0, columnspan=2)

    def addPlayer(self):
        values = {}
        for key in self.List:
            name = self.List[key].get()
            id_value = key.get()

            if id_value:
                values[int(id_value)] = name if name else ''

        returned_dict = python_supabase.Database.addData(values)
        for key, value in returned_dict.items():
            for key2 in self.List:
                id_value = key2.get()
                if value == None:
                    value = ''
                if id_value and int(id_value) == key:
                    self.List[key2].delete(0, END)
                    self.List[key2].config(state=NORMAL)
                    self.List[key2].insert(0, value)
                    # Enable the corresponding codename entry field
        self.getHardware(self.List)

    def getHardware(self, List: Dict):
        values = {}
        for key in List:
            if len(key.get()) > 0:
                values[int(key.get())] = self.popUpHardware(List[key].get())
        python_supabase.Database.addHardware(values)

    def popUpHardware(self, codename: str) -> int:
        top = Toplevel(self.master)
        top.geometry("250x250")
        self.hardwareID = 0
        Label(top, text=str(f'Enter Hardware ID for player: {codename}')).grid(
            row=0, column=0)
        entry = Entry(top, width=25)
        entry.grid(row=1, column=0)

        def submit_and_close():
            self.hardwareID = int(entry.get())
            top.destroy()

        Button(top, text="Submit", command=submit_and_close).grid(
            row=2, column=0)

        top.wait_window(top)  # Wait until the popup window is closed

        try:
            return int(self.hardwareID)
        except ValueError:
            return 0

    def insert_val(self, e, top) -> int:
        value = int(e.get())
        top.destroy()
        return value

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

        game_screen = GameScreen(self.master)
        game_screen.grid()


root = Tk()
app = Application(root)
# for testing functions
# root.bind("]", test.test())
print('running')
root.mainloop()
