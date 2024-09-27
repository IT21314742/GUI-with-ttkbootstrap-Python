from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb



root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap!")
#root.iconbitmap('images/codemy.ico')
root.geometry('500x350')

# Create a Function for the Button

# Create a Label
my_label = tb.Label(root, text="Hello Vihan!", font=("Poppins", 35),
                    bootstyle="warning, ")
my_label.pack(pady=50)

# Create a button
my_button = tb




root.mainloop()