# -*- coding: utf-8 -*-
while 1:
    count = input()
    step = 0
    string = []
    while step < count:
        temp = []
        operation = raw_input()
        operation = operation.split()
        if int(operation[0]) == 1:
            string.append(operation[1])
        elif int(operation[0]) == 2:
            temp.append(operation[1])
            temp.extend(string)
            string = temp
        step += 1
    print "".join(string)
