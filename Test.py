from RefSystem import *


rs = RefSystem("Example.txt")
rs.initFromCSV()
rs.initGrid()
rs.run()
rs.saveGridToData()
rs.saveToCSV()


print("Hello")

