import json
from dotenv import load_dotenv
from supabase import create_client, Client
from faker import Faker
import faker_commerce
import socket
from tkinter import *
from PIL import ImageTk, Image

def add_entries_to_vendor_table(supabase, name, codename):
    fake = Faker()
    foreign_key_list = []
    fake.add_provider(faker_commerce.Provider)
    main_list = []
    value = {'id': name, 'codename': codename}
    main_list.append(value)
    data = supabase.table('player').insert(main_list).execute()
    print(data)
    data_dict = data.dict()
    data_entries = data_dict['data']
    for entry in data_entries:
        foreign_key_list.append(int(entry['id']))
    return foreign_key_list

def add_entries_to_product_table(supabase, vendor_id):
    fake = Faker()
    fake.add_provider(faker_commerce.Provider)
    main_list = []
    iterator = fake.random_int(1, 15)
    for i in range(iterator):
        value = {'id': vendor_id, 'codename': fake.ecommerce_name()}
        main_list.append(value)
    data = supabase.table('Product').insert(main_list).execute()

class GameScreen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Game Screen")
        self.master.resizable(False, False)
        self.createWidgets()
        # add game stuffs

    def createWidgets(self):
        red = '#990000'
        green = '#346C4E'

        Label(text='Red Team', bg=red, fg='white', padx=10, pady=10).grid(row=0, column=0, columnspan=2)
        Label(text='Green Team', bg=green, fg='white', padx=20, pady=20).grid(row=0, column=2, columnspan=2)
        Label(text='Codename', bg=red, fg='white').grid(row=1, column=0)
        Label(text='Points', bg=red, fg='white').grid(row=1, column=1)
        Label(text='Codename', bg=green, fg='white').grid(row=1, column=2)
        Label(text='Points', bg=green, fg='white').grid(row=1, column=3)

        # Red Team
        for i in range(5):
            sv = StringVar()
            names = StringVar()
            entry = Entry(bg="white", fg="black", bd=2, textvariable=sv)
            entry.config(justify="right", selectbackground="#D8D8D8", font=('Times 18'), highlightbackground=red,
                         highlightcolor=red)
            entry.grid(row=i + 2, column=1)

            entry2 = Entry(bg="white", fg="black", bd=2, textvariable=names)
            entry2.config(justify="right", selectbackground="#D8D8D8", font=('Times 18'), highlightbackground=red,
                          highlightcolor=red, width=9)
            entry2.grid(row=i + 2, column=0)
            sv.trace("w", lambda name, index, mode, sv=sv: self.getName(sv, entry, names, entry2))
            names.trace("w", lambda name, index, mode, names=names: self.getName(sv, entry, names, entry2))

        # Green Team
        for i in range(5):
            Entry(bg="white", fg="black", bd=2, justify="right", selectbackground="#D8D8D8", font=('Times 18'),
                  highlightbackground=green, highlightcolor=green).grid(row=i + 2, column=3)
        for i in range(5):
            Entry(bg="white", fg="black", bd=2, justify="right", selectbackground="#D8D8D8", font=('Times 18'),
                  highlightbackground=green, highlightcolor=green, width=9).grid(row=i + 2, column=2)

class Application(Frame):
    id = [0]
    codename = [""]
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

        Label(text='Red Team', bg=red, fg='white', padx=20, pady=20).grid(row=0, column=0, columnspan=2)
        Label(text='Green Team', bg=green, fg='white', padx=20, pady=20).grid(row=0, column=2, columnspan=2)
        Label(text='ID', bg=red, fg='white').grid(row=1, column=0)
        Label(text='Codename', bg=red, fg='white').grid(row=1, column=1)
        Label(text='ID', bg=green, fg='white').grid(row=1, column=2)
        Label(text='Codename', bg=green, fg='white').grid(row=1, column=3)

        for i in range(15):
            sv = StringVar()
            names = StringVar()
            entry = Entry(bg="white", fg="black", bd=2, textvariable=sv)
            entry.config(justify="right", selectbackground="#D8D8D8", font=('Times 18'), highlightbackground=red,
                         highlightcolor=red)
            entry.grid(row=i + 2, column=1)

            entry2 = Entry(bg="white", fg="black", bd=2, textvariable=names)
            entry2.config(justify="right", selectbackground="#D8D8D8", font=('Times 18'), highlightbackground=red,
                          highlightcolor=red, width=9)
            entry2.grid(row=i + 2, column=0)
            sv.trace("w", lambda name, index, mode, sv=sv: self.getName(sv, entry, names, entry2))
            names.trace("w", lambda name, index, mode, names=names: self.getName(sv, entry, names, entry2))

        for i in range(15):
            Entry(bg="white", fg="black", bd=2, justify="right", selectbackground="#D8D8D8", font=('Times 18'),
                  highlightbackground=green, highlightcolor=green).grid(row=i + 2, column=3)
        for i in range(15):
            Entry(bg="white", fg="black", bd=2, justify="right", selectbackground="#D8D8D8", font=('Times 18'),
                  highlightbackground=green, highlightcolor=green, width=9).grid(row=i + 2, column=2)

    def getName(self, sv, entry, names, entry2):
        with open("player.sql", "r") as f:
            index = 0
            for line in f:
                word = f.readline()
                if f"VALUES ({names.get()}," in word:
                    code = word[10:-2]
                    index += 1
                    entry.setvar(names, code)
                    sv.set(code)
                else:
                    break
        with open("player.sql", "a") as f:
            nam = sv.get()
            idd = names.get()
            if nam != '':
                print('nam = ', nam)
                self.codename.append(nam)
            if idd is not None:
                if idd == '':
                    idd = -1
                self.id.append(int(idd))
            f.write(f"\nVALUES ({names.get()}, {sv.get()});")

    def createButton(self):
        Button(text="Submit ID", command=self.addData).grid(row=18, column=1, columnspan=2)
        Button(text="F5: Start Game", command=self.startGame).grid(row=19, column=2, columnspan=2)

    def startGame(self):
        # Clear existing widgets
        for widget in self.master.winfo_children():
            widget.destroy()

        # Create new game screen with 5 rows
        game_screen = GameScreen(self.master)
        game_screen.grid()

    def addData(self):
        load_dotenv()
        url: str = "https://rqavdtetomzeacidtuys.supabase.co"
        key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJxYXZkdGV0b216ZWFjaWR0dXlzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwNzQyMzc4MCwiZXhwIjoyMDIyOTk5NzgwfQ.6IKKyRyCOJjHYe-2-TsvoN7LF-wgChURyVxSrR2RgnQ"
        supabase: Client = create_client(url, key)
        id = self.id.pop()
        name = self.codename.pop()
        print('id = ', id, ' name = ', name)
        fk_list = add_entries_to_vendor_table(supabase, id, name)

root = Tk()
app = Application(root)
root.mainloop()
