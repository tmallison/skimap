from tkinter import *


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Skimap GUI")

        self.canvas = Canvas(master, bg='white', height=1000, width=1400)
        self.canvas.bind("<Button-1>", self.add_node)
        self.canvas.pack(side=RIGHT)

        self.label = Label(master, text="Add item")
        self.label.pack()

        self.add_node_button = Button(master, text="Add Nodes", command=self.toggle_add_node_button, relief="raised")
        self.add_node_button.pack()

        self.delete_node_button = Button(master, text="Delete Nodes", command=self.toggle_delete_node_button, relief="raised")
        self.delete_node_button.pack()

        self.save_button = Button(master, text="Save", command=self.save)
        self.save_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def save(self):
        print(self.canvas.find_withtag("node"))

    def add_node(self, event):
        if self.is_adding_nodes():
            x = event.x
            y = event.y

            oval_id = self.canvas.create_oval(x, y, x+20, y+20, fill="white", outline="red", width=5, tags="node")
            self.canvas.tag_bind(oval_id, "<Button-1>", self.connect_nodes)

    def connect_nodes(self, event):
        print(event.widget)

        if self.is_deleting_nodes():
            event.widget.delete("current")

    def toggle_add_node_button(self):
        if self.add_node_button.config('relief')[-1] == 'sunken':
            self.add_node_button.config(relief="raised")
        else:
            self.add_node_button.config(relief="sunken")

    def is_adding_nodes(self):
        return self.add_node_button.config('relief')[-1] == 'sunken'

    def toggle_delete_node_button(self):
        if self.delete_node_button.config('relief')[-1] == 'sunken':
            self.delete_node_button.config(relief="raised")
        else:
            self.delete_node_button.config(relief="sunken")

    def is_deleting_nodes(self):
        return self.delete_node_button.config('relief')[-1] == 'sunken'

root = Tk()
my_gui = GUI(root)
root.mainloop()
