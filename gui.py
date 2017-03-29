from Tkinter import *
import tkMessageBox
import info_processing
import map_data
import json

data = info_processing.json_load()


class GUI(Frame):
    # Initialize frame in a canvas, set scrollbars
    def __init__(self, root):
        Frame.__init__(self, root)
        self.canvas = Canvas(root, borderwidth=0)
        self.frame = Frame(self.canvas)
        self.innerframe = Frame(self.canvas)
        self.vbar = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.hbar = Scrollbar(root, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.vbar.set, xscrollcommand=self.hbar.set)
        self.vbar.pack(side="right", fill="y")
        self.hbar.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw", tags="self.frame")
        self.canvas.create_window((425, 0), window=self.innerframe, anchor="sw", tags="self.innerframe")
        self.frame.bind("<Configure>", self.on_frame_configure)
        self.innerframe.bind("<Configure>", self.on_frame_configure)
        root.protocol("WM_DELETE_WINDOW", self.quit)

        # Each checkbutton needs its own unique IntVar to select and deselect it correctly
        # The variable is 0 or 1, representing not collected and collected respectively
        # So when the checkbuttons are created, they are automatically checked if collected and vice versa
        self.vars = {0: IntVar(value=data[0]["collected"]), 1: IntVar(value=data[1]["collected"]), 2: IntVar(value=data[2]["collected"]), 3: IntVar(value=data[3]["collected"]), 4: IntVar(value=data[4]["collected"]),
                     5: IntVar(value=data[5]["collected"]), 6: IntVar(value=data[6]["collected"]), 7: IntVar(value=data[7]["collected"]), 8: IntVar(value=data[8]["collected"]), 9: IntVar(value=data[9]["collected"]),
                     10: IntVar(value=data[10]["collected"]), 11: IntVar(value=data[11]["collected"]), 12: IntVar(value=data[12]["collected"]), 13: IntVar(value=data[13]["collected"]), 14: IntVar(value=data[14]["collected"]),
                     15: IntVar(value=data[15]["collected"]), 16: IntVar(value=data[16]["collected"]), 17: IntVar(value=data[17]["collected"]), 18: IntVar(value=data[28]["collected"]), 19: IntVar(value=data[19]["collected"]),
                     20: IntVar(value=data[20]["collected"]), 21: IntVar(value=data[21]["collected"]), 22: IntVar(value=data[22]["collected"]), 23: IntVar(value=data[23]["collected"]), 24: IntVar(value=data[24]["collected"]),
                     25: IntVar(value=data[25]["collected"]), 26: IntVar(value=data[26]["collected"]), 27: IntVar(value=data[27]["collected"]), 28: IntVar(value=data[28]["collected"]), 29: IntVar(value=data[29]["collected"]),
                     30: IntVar(value=data[30]["collected"]), 31: IntVar(value=data[31]["collected"]), 32: IntVar(value=data[32]["collected"]), 33: IntVar(value=data[33]["collected"]), 34: IntVar(value=data[34]["collected"]),
                     35: IntVar(value=data[35]["collected"]), 36: IntVar(value=data[36]["collected"]), 37: IntVar(value=data[37]["collected"]), 38: IntVar(value=data[38]["collected"]), 39: IntVar(value=data[39]["collected"]),
                     40: IntVar(value=data[40]["collected"]), 41: IntVar(value=data[41]["collected"]), 42: IntVar(value=data[42]["collected"]), 43: IntVar(value=data[43]["collected"]), 44: IntVar(value=data[44]["collected"]),
                     45: IntVar(value=data[45]["collected"]), 46: IntVar(value=data[46]["collected"]), 47: IntVar(value=data[47]["collected"]), 48: IntVar(value=data[48]["collected"]), 49: IntVar(value=data[49]["collected"])}

        self.main()

    # When the user exits the window, they are asked if they are sure,
    # if so the data.json file is rewritten with updated information
    def quit(self):
        if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
            with open('data.json', "w") as f:
                json.dump(data, f)
            # Save a new version of collected states each time the program runs
            map_data.get_overall_map(self.collected)
            root.destroy()

    # Reset scroll frame to encompass inner frame
    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    # When a picture of a coin is clicked, a new window pops up with more detailed information
    @staticmethod
    def new_window(num):
        w = Toplevel(root)
        newtext = Text(w)
        newtext.insert(END, "Design description: " + data[num]["description"] + "\n")
        newtext.insert(END, "Date issued: " + data[num]["date_issued"])
        newtext.image_create(END, image=maps[num])
        newtext.pack(side=LEFT, fill=BOTH)

    # Edits the data file whenever a checkbutton is clicked so when the program closes,
    # the data.json file can be rewritten with the updated information
    @staticmethod
    def callback(x):
        if data[x]["collected"]:
            data[x]["collected"] = 0
        else:
            data[x]["collected"] = 1
        # So the user can be sure the right checkbuttons are being recorded
        print("Checkbutton #" + str(x+1) + " was changed")

    # Create each column on the fly so I don't have to create 50 separate checkbuttons
    # Inner column 1 is a label showing number and state, as such: "1: Delaware"
    # Inner column 2 is a button with the image of the state's coin on it, when clicked it opens a new window with more information
    # Inner column 3 is another label that always says "Collected?" to label the checkbutton on its right
    # Inner column 4 is the checkbutton itself, each given a unique name and variable
    # The 4 inner columns represent 1 state, full grid is 5x10 so 20 total columns and 10 total rows
    def column1(self):
        for x in range(10):
            Label(self.frame, text=str(x + 1) + ": " + data[x]["state"]).grid(row=x, column=0)
            Button(self.frame, image=self.images[x], command=lambda a=x: self.new_window(a)).grid(row=x, column=1)
            Label(self.frame, text="Collected?").grid(row=x, column=2)
            check1 = Checkbutton(self.frame, name="checkbutton" + str(x), variable=self.vars[x], command=lambda a=x: self.callback(a))
            check1.grid(row=x, column=3)

    def column2(self):
        for x in range(10):
            Label(self.frame, text=str(x + 11) + ": " + data[x + 10]["state"]).grid(row=x, column=4)
            Button(self.frame, image=self.images[x + 10], command=lambda a=x+10: self.new_window(a)).grid(row=x, column=5)
            Label(self.frame, text="Collected?").grid(row=x, column=6)
            check = Checkbutton(self.frame, name="checkbutton" + str(x + 10), variable=self.vars[x+10], command=lambda a=x+10: self.callback(a))
            check.grid(row=x, column=7)

    def column3(self):
        for x in range(10):
            Label(self.frame, text=str(x + 21) + ": " + data[x + 20]["state"]).grid(row=x, column=8)
            Button(self.frame, image=self.images[x + 20], command=lambda a=x+20: self.new_window(a)).grid(row=x, column=9)
            Label(self.frame, text="Collected?").grid(row=x, column=10)
            check = Checkbutton(self.frame, name="checkbutton" + str(x + 20), variable=self.vars[x+20], command=lambda a=x+20: self.callback(a))
            check.grid(row=x, column=11)

    def column4(self):
        for x in range(10):
            Label(self.frame, text=str(x + 31) + ": " + data[x + 30]["state"]).grid(row=x, column=12)
            Button(self.frame, image=self.images[x + 30], command=lambda a=x+30: self.new_window(a)).grid(row=x, column=13)
            Label(self.frame, text="Collected?").grid(row=x, column=14)
            check = Checkbutton(self.frame, name="checkbutton" + str(x + 30), variable=self.vars[x+30], command=lambda a=x+30: self.callback(a))
            check.grid(row=x, column=15)

    def column5(self):
        for x in range(10):
            Label(self.frame, text=str(x + 41) + ": " + data[x + 40]["state"]).grid(row=x, column=16)
            Button(self.frame, image=self.images[x + 40], command=lambda a=x+40: self.new_window(a)).grid(row=x, column=17)
            Label(self.frame, text="Collected?").grid(row=x, column=18)
            check = Checkbutton(self.frame, name="checkbutton" + str(x + 40), variable=self.vars[x+40], command=lambda a=x+40: self.callback(a))
            check.grid(row=x, column=19)

    def master_button(self):
        b = Button(self.innerframe, command=lambda a=self.collected, b=self.uncollected: self.master_info(a, b))
        b.config(image=mastermap)
        b.image = mastermap
        b.pack(side="bottom")

    # When the master map is clicked, a window pops up with a list of all states collected and uncollected
    def master_info(self, collected, uncollected):
        def frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        w = Toplevel(root)
        Frame.__init__(self, w)
        canvas = Canvas(w, borderwidth=0)
        frame = Frame(canvas)
        vbar = Scrollbar(w, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vbar.set)
        vbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0, 0), window=frame, anchor="nw")
        frame.bind("<Configure>", frame_configure)

        Label(frame, text="States you have collected:").grid(row=0, column=0)
        Label(frame, text="\tStates you have not collected:").grid(row=0, column=1)
        for x in range(len(collected)):
            Label(frame, text=collected[x]).grid(row=x+1, column=0)
        for x in range(len(uncollected)):
            Label(frame, text="\t" + uncollected[x]).grid(row=x+1, column=1)

    # Setup: set title, populate images and vars lists, create table
    def main(self):
        root.title("Coin Collection Helper")
        self.images = []
        self.vars = []
        self.collected = []
        self.uncollected = []
        for x in range(50):
            photo = PhotoImage(file="images/coin/coin" + str(x) + ".gif")
            self.images.append(photo)
            if data[x]["collected"] == 1:
                self.vars.append(IntVar(value=1))
                self.collected.append(data[x]["state"])
            else:
                self.vars.append(IntVar(value=0))
                self.uncollected.append(data[x]["state"])

        self.column1()
        self.column2()
        self.column3()
        self.column4()
        self.column5()
        self.master_button()

if __name__ == "__main__":
    root = Tk()
    root.state('zoomed')
    maps = info_processing.convert_images()
    mastermap = info_processing.get_mastermap()
    gui = GUI(root)
    root.mainloop()
