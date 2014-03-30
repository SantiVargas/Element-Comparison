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
    file = open("C:/users/user/Desktop/artist_lists_small.txt", "r", encoding="UTF8");
    numList = {};
    bandList = [];
    numList, bandList = readValues(file, 50);
    print(time.clock() - start);
