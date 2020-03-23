import tkinter as tk
import csv

class RefSystem(object):

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Referee system')
        self.root.geometry('700x400')
        self.data = []
    
    def run(self):
        tk.mainloop()

    def initFromCSV(self, filename):
        """
        Column 1: Day
        Column 2: Month
        Column 3: Club
        Column 4: Travel money
        Column 5: Salary
        """
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=";")

            for row in csv_reader:
                self.data.append(row)
            

    def initGrid(self):
        
        for i in range(len(self.data)):
            for j in range(len(self.data[1])):
                e = tk.Entry(self.root)
                e.insert(tk.END, self.data[i][j])
                e.grid(row = i, column = j)