import csv

class VegData:
  def __init__(self,):
    self.vegDict = {}
    with open('VegNut.csv', newline='') as csvfile:
      vegetablesInfo = csv.reader(csvfile, delimiter=',')
      i = 0
      keys = []   
      for row in vegetablesInfo:
          if (i==0):
              keys = row
          else:
              self.vegDict[row[0]] = {keys[1]:float(row[1]), keys[2]:float(row[2]), keys[3]:float(row[3]), keys[4]:float(row[4]),
                                keys[5]:float(row[5])}
          i += 1   

  def printDict(self):
    print(self.vegDict)
  
  def calcFitness(self, gardenPlot):
    print(gardenPlot)
     


