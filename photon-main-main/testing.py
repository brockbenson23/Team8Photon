import json
from dotenv import load_dotenv
from supabase import create_client, Client
from faker import Faker
import faker_commerce
from tkinter import *
from PIL import ImageTk
from PIL import Image as im


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
    data_json = json.dumps(data_dict)
    data_entries = data_json['data']
    for i in range(len(data_entries)):
        foreign_key_list.append(int(data_entries[i]['id']))
    return foreign_key_list


class SplashScreen(Tk):
    def __init__(self):
        super().__init__()
        self.title("Team8Photon")
        self.geometry("700x700")

        path = "logo.jpg"
        img = ImageTk.PhotoImage(im.open(path))
        original_image = im.open(path)
        resized_image = original_image.resize((700, 700))
        img = ImageTk.PhotoImage(resized_image)
        label = Label(self, image=img)
        label.grid()

        self.after(3000, self.destroy)
        self.mainloop()


class TeamEntry(Frame):
    list = []

    def __init__(self, master, color, column_offset, team_name, entry_list):
        super().__init__(master, background=color)
        self.master = master
        self.team_name = team_name
        self.grid(row=0, column=column_offset, columnspan=2)
        self.create_widgets()
        self.list = entry_list

    def create_widgets(self):
        Label(self, text=self.team_name + ' Team', bg=self.cget("background"),
              fg='white', padx=20, pady=20).grid(row=0, column=0, columnspan=2)
        Label(self, text='ID', bg=self.cget("background"),
              fg='white').grid(row=1, column=0)
        Label(self, text='Codename', bg=self.cget(
            "background"), fg='white').grid(row=1, column=1)

        i = 0

        for entry in self.list:
            self.entry = Entry(entry)
            self.entry.grid(row=i, column=2)
            i += 1
#       red2 = Entry(self, bg="white", fg="black", bd=2, justify="right", selectbackground="#D8D8D8",
#                     font=('Times 18'), highlightbackground=self.cget("background"), highlightcolor=self.cget("background"))
#       red2.grid(row=3, column=3)
#       red3 = Entry(self, bg="white", fg="black", bd=2, justify="right", selectbackground="#D8D8D8",
#                     font=('Times 18'), highlightbackground=self.cget("background"), highlightcolor=self.cget("background"))
#       red3.grid(row=4, column=3)
#       red4= Entry(self, bg="white", fg="black", bd=2, justify="right", selectbackground="#D8D8D8",
#                     font=('Times 18'), highlightbackground=self.cget("background"), highlightcolor=self.cget("background"))
#       red4.grid(row=5, column=3)

#       red5= Entry(self, bg="white", fg="black", bd=2, justify="right", selectbackground="#D8D8D8",
#                     font=('Times 18'), highlightbackground=self.cget("background"), highlightcolor=self.cget("background"))
#       red5.grid(row=6, column=3)

#       red6= Entry(self, bg="white", fg="black", bd=2, justify="right", selectbackground="#D8D8D8",
#                     font=('Times 18'), highlightbackground=self.cget("background"), highlightcolor=self.cget("background"))
#       red6.grid(row=7, column=3)

#       red7 = Entry(self, bg="white", fg="black", bd=2, justify="right", selectbackground="#D8D8D8",
#                     font=('Times 18'), highlightbackground=self.cget("background"), highlightcolor=self.cget("background"))
#       red7.grid(row=8, column=3)

#       for i in range(15):
#           sv = StringVar()
#           names = StringVar()
#           entry = Entry(self, bg="white", fg="black", bd=2, textvariable=sv, justify="right", selectbackground="#D8D8D8",
#                         font=('Times 18'), highlightbackground=self.cget("background"), highlightcolor=self.cget("background"))
#           entry.grid(row=i+2, column=1)
#           entry2 = Entry(self, bg="white", fg="black", bd=2, textvariable=names, justify="right", selectbackground="#D8D8D8",
#                          font=('Times 18'), highlightbackground=self.cget("background"), highlightcolor=self.cget("background"), width=9)
#           entry2.grid(row=i+2, column=0)
#           sv.trace("w", lambda name, index, mode,
#                    sv=sv: self.get_name(sv, entry, names, entry2))
#           names.trace("w", lambda name, index, mode,
#                       names=names: self.get_name(sv, entry, names, entry2))

    def get_name(self, sv, entry, names, entry2):
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
                self.master.codename.append(nam)
            if idd is not None:
                if idd == '':
                    idd = -1
                self.master.id.append(int(idd))
            f.write(f"\nVALUES ({names.get()}, {sv.get()});")


class Application(Frame):
    red1 = Entry(bg="white", fg="black", bd=2, justify="right", selectbackground="#D8D8D8", font=(
        'Times 18'))
    entries = [red1]

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Team8Photon")
        self.master.resizable(False, False)
        self.id = [0]
        self.codename = [""]
        self.grid()
        self.create_teams()
        self.create_button()

    def create_teams(self):
        TeamEntry(self, "#990000", 0, "Red", self.entries)
        TeamEntry(self, "#346C4E", 2, "Green", self.entries)

    def create_button(self):
        button = Button(text="Submit ID", command=self.add_data)
        button.grid(row=19, column=1, columnspan=2)
        test_button = Button(text="TEST", command=self.testing)
        test_button.grid(row=20, column=0, columnspan=1)

    def testing(self):
        print('in testing')
        text = self.entry.get()
        print(text)
        return "testing"

    def add_data(self):
        load_dotenv()
        url = "https://rqavdtetomzeacidtuys.supabase.co"
        key = "YOUR_SUPABASE_KEY"
        supabase = create_client(url, key)
        id = self.id.pop()
        name = self.codename.pop()
        print('id = ', id, ' name = ', name)
        add_entries_to_vendor_table(supabase, id, name)


# splash = SplashScreen()
root = Tk()
app = Application(root)
root.mainloop()
