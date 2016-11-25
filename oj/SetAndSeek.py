# -*- coding: utf-8 -*-
while 1:
    setNums = raw_input()
    setNums = setNums.split()
    setOneTemp = raw_input()
    setTwoTemp = raw_input()
    setOneTemp = setOneTemp.split()
    setTwoTemp = setTwoTemp.split()
    setOne = []
    setTwo = []
    for i in setOneTemp:
        setOne.append(int(i))
    for i in setTwoTemp:
        setTwo.append(int(i))
    tmp = list(set(setOne).union(set(setTwo)))
    tmp.sort()
    temp = []
    for i in tmp:
        temp.append(str(i))
    print " ".join(temp)