from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# root = Tk()

# def browsefunc():
#     filename = filedialog.askopenfilename()
#     print(filename)

# browsebutton = Button(root, text="Browse", command=browsefunc)
# browsebutton.pack()

# pathlabel = Label(root)
# pathlabel.pack()

class Controls():
    
    def find_files():
        filename = filedialog.askopenfilenames()
        print(filename)
