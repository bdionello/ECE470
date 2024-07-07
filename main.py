import csv
vegDict = {}
with open('VegNut.csv', newline='') as csvfile:
    vegetablesInfo = csv.reader(csvfile, delimiter=',')
    #vegDict = dict((rows[0],rows[1]) for rows in vegetablesInfo)
    #print(vegDict)
    i = 0
    keys = []   
    for row in vegetablesInfo:
        if (i==0):
            keys = row
        else:
            vegDict[row[0]] = {keys[1]:row[1], keys[2]:row[2], keys[3]:row[3], keys[4]:row[4],
                               keys[5]:row[5]}
        i += 1 
    print(vegDict)
