import tkinter as tk

class RefSystem(object):

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Referee system')
        self.root.geometry('700x400')
    
    def run(self):
        tk.mainloop()
