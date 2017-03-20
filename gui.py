from tkinter import *
from tkinter import ttk
import info_processing

root = Tk()
root.title("Coin Collection Helper")

data = info_processing.json_load()

root.mainloop()