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

def main():
    import time;
    start = time.clock();
    file = open("Artist-list.txt", "r", encoding="UTF8");
    numList = {};
    bandList = [];
    numList, bandList = readValues(file, 50);    
    lol = [];#list of lists
    #go through list marking off matching bands and removing lists without more than 2
    for b in bandList:
        temp = b.split(",");
        tempList = [];
        for band in numList:            
            if band in temp:
                tempList.append(1);
            else:
                tempList.append(0);
        if tempList.count(1) > 2:
            lol.append(tempList);
    print ("Time Taken:", time.clock() - start);
    print(len(lol));
    file.close();
