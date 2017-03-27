from tkinter import *
import info_processing

data = info_processing.json_load()


class GUI(Frame):
    # Initialize frame in a canvas, set scrollbars
    def __init__(self, root):
        Frame.__init__(self, root)
        self.canvas = Canvas(root, borderwidth=0)
        self.frame = Frame(self.canvas)
        self.vbar = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.hbar = Scrollbar(root, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.vbar.set, xscrollcommand=self.hbar.set)
        self.vbar.pack(side="right", fill="y")
        self.hbar.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 50), window=self.frame, anchor="nw", tags="self.frame")
        self.frame.bind("<Configure>", self.on_frame_configure)
        self.main()

    def quit(self):
        root.quit()

    # Reset scroll frame to encompass inner frame
    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    # When a picture of a coin is clicked, a new window pops up with more detailed information
    def new_window(self, num):
        w = Toplevel(root)
        newtext = Text(w)
        newtext.insert(END, "Design description: " + data[num]["description"] + "\n")
        newtext.insert(END, "Date issued: " + data[num]["date_issued"])
        newtext.pack(side=LEFT, fill=BOTH)

    def column1(self):
        for x in range(10):
            Label(self.frame, text=str(x + 1) + ": " + data[x]["state"]).grid(row=x, column=0)
            Button(self.frame, image=self.images[x], command=lambda a=x: self.new_window(a), borderwidth=2).grid(row=x, column=1)
            Label(self.frame, text="Collected?", borderwidth=2).grid(row=x, column=2)
            self.selection = BooleanVar()
            check = Checkbutton(self.frame, name="checkbutton" + str(x), variable=self.selection, borderwidth=2)
            check.grid(row=x, column=3)

    def column2(self):
        for x in range(10):
            Label(self.frame, text=str(x + 11) + ": " + data[x + 10]["state"]).grid(row=x, column=4)
            Button(self.frame, image=self.images[x + 10], command=lambda a=x+10: self.new_window(a), borderwidth=2).grid(row=x, column=5)
            Label(self.frame, text="Collected?", borderwidth=2).grid(row=x, column=6)
            self.selection = BooleanVar()
            check = Checkbutton(self.frame, name="checkbutton" + str(x), variable=self.selection, borderwidth=2)
            check.grid(row=x, column=7)

    def column3(self):
        for x in range(10):
            Label(self.frame, text=str(x + 21) + ": " + data[x + 20]["state"]).grid(row=x, column=8)
            Button(self.frame, image=self.images[x + 20], command=lambda a=x+20: self.new_window(a), borderwidth=2).grid(row=x, column=9)
            Label(self.frame, text="Collected?", borderwidth=2).grid(row=x, column=10)
            self.selection = BooleanVar()
            check = Checkbutton(self.frame, name="checkbutton" + str(x), variable=self.selection, borderwidth=2)
            check.grid(row=x, column=11)

    def column4(self):
        for x in range(10):
            Label(self.frame, text=str(x + 31) + ": " + data[x + 30]["state"]).grid(row=x, column=12)
            Button(self.frame, image=self.images[x + 30], command=lambda a=x+30: self.new_window(a), borderwidth=2).grid(row=x, column=13)
            Label(self.frame, text="Collected?", borderwidth=2).grid(row=x, column=14)
            self.selection = BooleanVar()
            check = Checkbutton(self.frame, name="checkbutton" + str(x), variable=self.selection, borderwidth=2)
            check.grid(row=x, column=15)

    def column5(self):
        for x in range(10):
            Label(self.frame, text=str(x + 41) + ": " + data[x + 40]["state"]).grid(row=x, column=16)
            Button(self.frame, image=self.images[x + 40], command=lambda a=x+40: self.new_window(a), borderwidth=2).grid(row=x, column=17)
            Label(self.frame, text="Collected?", borderwidth=2).grid(row=x, column=18)
            self.selection = BooleanVar()
            check = Checkbutton(self.frame, name="checkbutton" + str(x), variable=self.selection, borderwidth=2)
            check.grid(row=x, column=19)

    # Setup
    def main(self):
        root.title("Coin Collection Helper")
        self.selection = BooleanVar()
        self.images = []
        self.buttons = []
        self.vars = []
        for x in range(50):
            photo = PhotoImage(file="images/coin" + str(x) + ".gif")
            self.images.append(photo)

        self.column1()
        # self.column2()
        # self.column3()
        # self.column4()
        # self.column5()

if __name__ == "__main__":
    root = Tk()
    gui = GUI(root)
    root.mainloop()
