# -*- coding: utf-8 -*-
from collections import deque
while 1:
    count = input()
    step = 0
    string = deque([])
    while step < count:
        operationInput = raw_input()
        operationInput = operationInput.split()
        if int(operationInput[0]) == 1:
            string.append(operationInput[1])
        elif int(operationInput[0]) == 2:
            string.appendleft(operationInput[1])
        step += 1
    print ''.join(string)
