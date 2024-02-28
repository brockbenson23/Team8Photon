#import os
import json
from dotenv import load_dotenv
from supabase import create_client, Client
from faker import Faker
import faker_commerce


def add_entries_to_vendor_table(supabase, name, codename):
    fake = Faker()
    foreign_key_list = []
    fake.add_provider(faker_commerce.Provider)
    main_list = []
    value = {'id': name,'codename': codename}

    main_list.append(value)
    data = supabase.table('player').insert(main_list).execute()
    print(data)
    data_dict = data.dict()
    data_json = json.dumps(data_dict)
    data_entries = data_json['data']
    for i in range(len(data_entries)):
        foreign_key_list.append(int(data_entries[i]['id']))
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


def main():
    vendor_count = 10
    load_dotenv()
    url: str = "https://rqavdtetomzeacidtuys.supabase.co"
    key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJxYXZkdGV0b216ZWFjaWR0dXlzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwNzQyMzc4MCwiZXhwIjoyMDIyOTk5NzgwfQ.6IKKyRyCOJjHYe-2-TsvoN7LF-wgChURyVxSrR2RgnQ"
    supabase: Client = create_client(url, key)


#Import required libraries
# from tkinter import *
# from PIL import ImageTk, Image as im

# Import required libraries
import socket
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
    id = [0]
    codename = [""]

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
        self.createButton()
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
            sv = StringVar()
            names = StringVar()
            self.entry = Entry(bg="white", fg="black", bd=2, textvariable=sv)
            self.entry.config(justify="right", selectbackground="#D8D8D8", font=('Times 26'), highlightbackground=red,
                              highlightcolor=red)
            self.entry.grid(row=i+2, column=1)

            self.entry2 = Entry(bg="white", fg="black",
                                bd=2, textvariable=names)
            self.entry2.config(justify="right", selectbackground="#D8D8D8", font=('Times 26'), highlightbackground=red,
                               highlightcolor=red, width=9)
            self.entry2.grid(row=i+2, column=0)
            sv.trace("w", lambda name, index, mode, sv=sv: getName(
                sv, self.entry, names, self.entry2))
            names.trace("w", lambda name, index, mode, names=names: getName(
                sv, self.entry, names, self.entry2))

        for i in range(15):
            self.entry = Entry(bg="white", fg="black", bd=2)
            self.entry.config(justify="right", selectbackground="#D8D8D8", font=('Times 26'), highlightbackground=green,
                              highlightcolor=green)
            self.entry.grid(row=i+2, column=3)
        for i in range(15):
            self.entry = Entry(bg="white", fg="black", bd=2)
            self.entry.config(justify="right", selectbackground="#D8D8D8", font=('Times 26'), highlightbackground=green,
                              highlightcolor=green, width=9)
            self.entry.grid(row=i+2, column=2)

        def getName(sv, entry, names, entry2) -> None:
            f = open("player.sql", "r")
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
            f.close()
            f = open("player.sql", "a")
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

# make string with trace, use button to check when done typing

    def createButton(self):
        self.button = Button(text="Submit ID", command=self.addData)
        self.button.grid(row=18, column=1, columnspan=2)

    def addData(self) -> str:
        load_dotenv()
        url: str = "https://rqavdtetomzeacidtuys.supabase.co"
        key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJxYXZkdGV0b216ZWFjaWR0dXlzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwNzQyMzc4MCwiZXhwIjoyMDIyOTk5NzgwfQ.6IKKyRyCOJjHYe-2-TsvoN7LF-wgChURyVxSrR2RgnQ"
        supabase: Client = create_client(url, key)
        id = self.id.pop()
        name = self.codename.pop()
        print('id = ', id, ' name = ', name)
        fk_list = add_entries_to_vendor_table(supabase, id, name)
        return ""
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
