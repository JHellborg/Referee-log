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
        self.current_row = 0
        self.addNewButton()
        self.addFieldLabels()

    def onNewButton(self):
        self.dataVar.append([])
        self.data.append(self.data[0].copy())
        newLine = len(self.dataVar) - 1
        for i in range(len(self.data[0])):
            s = tk.StringVar()
            entry = tk.Entry(self.root, textvariable = s)
            entry.grid(row = self.current_row, column = i)
            self.dataVar[newLine].append(s)
        self.current_row += 1


    def addNewButton(self):
        self.newButton = tk.Button(self.root, command=self.onNewButton, text = "New")
        self.newButton.grid(row = self.current_row, column = 0)
        self.current_row += 1

    def addFieldLabels(self):
        dayLabel = tk.Label(self.root, text="Day")
        dayLabel.grid(row = self.current_row, column = 0, sticky=tk.W)
        dayLabel = tk.Label(self.root, text="Month")
        dayLabel.grid(row = self.current_row, column = 1, sticky=tk.W)
        dayLabel = tk.Label(self.root, text="Club")
        dayLabel.grid(row = self.current_row, column = 2, sticky=tk.W)
        dayLabel = tk.Label(self.root, text="Travel")
        dayLabel.grid(row = self.current_row, column = 3, sticky=tk.W)
        dayLabel = tk.Label(self.root, text="Salary")
        dayLabel.grid(row = self.current_row, column = 4, sticky=tk.W)
        self.current_row += 1

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
                e.grid(row = self.current_row, column = j)
                self.dataVar[i][j] = s
                self.grid[i][j] = e

            self.current_row += 1
                

    def saveGridToData(self):

        for i in range(len(self.dataVar)):
            for j in range(len(self.dataVar[0])):
                s = self.dataVar[i][j]
                self.data[i][j] = s.get()

    def saveToCSV(self):
        with open(self.filename, "w", newline='\n', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter = ";")

            for row in self.data:
                csv_writer.writerow(row)

