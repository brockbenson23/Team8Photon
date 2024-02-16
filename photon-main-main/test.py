# Import required libraries
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry("650x400")

# Initialize the file name in a variable
path = "logo.jpg"

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open(path))

# Create a Label Widget to display the text or Image
label = Label(win, image=img)
label.pack(fill="both")

win.mainloop()
