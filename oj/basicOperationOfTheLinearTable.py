# -*- coding: utf-8 -*-
while 1:
    count = input()
    step = 0
    string = []
    while step < count:
        operationInput = raw_input()
        operationInput = operationInput.split()
        if int(operationInput[0]) == 1:
            string.append(operationInput[1])
        elif int(operationInput[0]) == 2:
            string.insert(0, operationInput[1])
        elif int(operationInput[0]) == 3:
            string.pop(int(operationInput[1]) - 1)
        elif int(operationInput[0]) == 4:
            string.insert(int(operationInput[1]), operationInput[2])
        step += 1
    print ''.join(string)
