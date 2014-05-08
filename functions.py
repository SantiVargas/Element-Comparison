def readValues(f, minNum):
    theList = {};
    wholeList = [];
    for line in f:
        wholeList.append(line);
        tempList = line.split(",");
        for x in tempList:
            if x in theList:
                theList[x] += 1;
            else:
                theList[x] = 1;
    return trimList(theList, minNum), wholeList;

def trimList(bList, requirement):
    tempList = {};
    for x in bList:
        if bList[x] >= requirement:
            tempList[x] = bList[x];
    return tempList;

def populateBoolArrays(mainList, listToCompare):
    listOfLists = [];
    for line in mainList:
        bandsInLine = line.split(",");#see the next comment 
        tempList = [];
        for band in listToCompare:
            tempList.append(band in bandsInLine);#comparing band to line gives false positives. Ex: 'Queen' comapred to 'Queens' would be true
        if tempList.count(1) > 2:
            listOfLists.append(tempList);
    return listOfLists;

def main():
    #timing
    import time;
    start = time.clock();
    #file
    file = open("Artist-list.txt", "r", encoding="UTF8");

    numList = {};
    bandList = [];
    
    numList, bandList = readValues(file, 50);
    sortedBands = sorted(numList);
    
    lol = populateBoolArrays(bandList, sortedBands);    
            
    #compare bands
    #y - rows or ists of multiple bands
    #x and i - columns of answers for single bands
    matchList = [];
    for i in range(0, len(sortedBands) - 2):#subtracted 2 becasue there is no need to check the last column against itself
        for x in range(i+1, len(sortedBands) - 1):
            matches = 0;
            for y in range(0, len(lol) - 1):#can we subtract 2 because of the trailing '\n'?
                matches += lol[y][i] and lol[y][x];
            if matches > 50:
                matchList.append("" + sortedBands[i] + " and " + sortedBands[x]);

    print ("Time Taken:", time.clock() - start);
    print ("Total Matches: ", len(matchList));
    print ("Match List:");
    print (matchList);
    file.close();
