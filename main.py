import vegdata
import random 
minArea = 10
maxArea = 600
maxWater = 2000
# 1 pick a random number between 1 and vegList.len, use this to select a vegetable from the list
# 2 allocate a random number between some min and maxArea to this vegetable
# 3 allocate a random number betwee nsome min and Area Left
# 4 repeat 3 until no area is left

def main():
    myVeg = vegdata.VegData()
    #myVeg.printDict()
    vegList = list(myVeg.vegDict.keys())
    numVeg = len(vegList)
    print(vegList)
    gardenPlot = {}
    currentArea = maxArea
    while(1):
        selectedVeg = random.randrange(1, numVeg)
        selectedArea = random.randrange(minArea, currentArea)
        gardenPlot[vegList[selectedVeg]] = selectedArea
        currentArea = currentArea - selectedArea
        vegList.pop(selectedVeg)
        numVeg = numVeg - 1
        if currentArea <= minArea:
            break

    myVeg.calcFitness(gardenPlot)
    myVeg.printDict()

if __name__ == "__main__":
    main()    

