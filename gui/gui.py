from tkinter import *


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Skimap GUI")

        self.canvas = Canvas(master, bg='white', height=1000, width=1400)
        self.canvas.bind("<Button-1>", self.callback)
        self.canvas.pack(side=RIGHT)

        self.label = Label(master, text="Add item")
        self.label.pack()

        self.save_button = Button(master, text="Save", command=self.save)
        self.save_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def save(self):
        print(self.canvas.find_withtag("node"))

    def callback(self, event):
        x = event.x
        y = event.y

        print("clicked at", x, y)

        # self.canvas.create_rectangle(x, y, x+10, y+10, fill="black")
        self.canvas.create_oval(x, y, x+20, y+20, fill="white", outline="red", width=5, tags="node")



root = Tk()
my_gui = GUI(root)
root.mainloop()
