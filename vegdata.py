import csv

class VegData:
  def __init__(self,):
    self.vegDict = {}
    self.vegList = []
    with open('VegNut2.csv', newline='') as csvfile:
      vegetablesInfo = csv.reader(csvfile, delimiter=',')
      i = 0
      keys = []   
      for row in vegetablesInfo:
          if (i==0):
              keys = row
          else:
              self.vegDict[row[0]] = {keys[1]:float(row[1]), keys[2]:float(row[2])}
          i += 1
      self.vegList = list(self.vegDict.keys())
  def printDict(self):
    print(self.vegDict)

  def getFunct1(self):
    x = []
    for veg in self.vegDict:
      x.append(self.vegDict[veg]["CropScore"])
    return x
      
  def getFunct2(self):
    y = []
    for veg in self.vegDict:
      y.append(self.vegDict[veg]["ET"])
    return y     
  
     


