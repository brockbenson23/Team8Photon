import tkinter as tk
import os
from PIL import ImageTk, Image


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.img = None

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
                                    command=self.quit)

        self.quitButton.grid()
# Get the current script's directory
#        current_directory = os.path.dirname(os.path.realpath(__file__))

# Move up one directory to reach the parent directory
#       parent_directory = os.path.abspath(
#          os.path.join(current_directory, os.pardir))

# Construct the path to the photo
#     photo_path = os.path.join(parent_directory, 'redtower-arena.png')
        try:
            self.img = ImageTk.PhotoImage(Image.open('logo.jpg'))
        except Exception as e:
            print(f"Error loading image: {e}")

#        print(f"Photo path: {photo_path}")

        canvas = tk.Canvas(self, width=300, height=300)
        canvas.grid()
        canvas.create_image(20, 20, anchor=tk.NW, image=self.img)

        for i in range(15):
            self.entry = tk.Entry()
            self.entry.grid()
        for i in range(15):
            self.entry = tk.Entry()
            self.entry.grid(row=i+1, column=1)


app = Application()
app.mainloop()
