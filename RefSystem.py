import tkinter as tk
import csv

class RefSystem(object):

    def __init__(self, filename):
        self.root = tk.Tk()
        self.root.title('Referee system')
        self.root.geometry('700x400')
        self.data = []
        self.grid = []
        self.filename = filename
        self.dataVar = []
    
    def run(self):
        tk.mainloop()

    def initFromCSV(self):
        """
        Column 1: Day
        Column 2: Month
        Column 3: Club
        Column 4: Travel money
        Column 5: Salary
        """
        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=";")

            for row in csv_reader:
                self.data.append(row)
            

    def initGrid(self):
        

        for i in range(len(self.data)):
            self.grid.append(self.data[i].copy())
            self.dataVar.append(self.data[i].copy())
            for j in range(len(self.data[1])):
                s = tk.StringVar()
                s.set(self.data[i][j])
                e = tk.Entry(self.root, textvariable = s)
                e.grid(row = i, column = j)
                #e.pack()
                self.dataVar[i][j] = s
                self.grid[i][j] = e
                

    def saveGridToData(self):

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                s = self.dataVar[i][j]
                self.data[i][j] = s.get()

    def saveToCSV(self):
        with open(self.filename, "w", newline='\n', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter = ";")

            for row in self.data:
                csv_writer.writerow(row)

