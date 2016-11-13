# -*- coding: utf-8 -*-
class Stack():
    def __init__(self):
        self.items = []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

    def clear(self):
        del self.items[:]

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[self.size() - 1]


while (1):
    s = Stack()
    nums = input()
    # tarins生成入栈序列
    trains = [x for x in range(1, nums + 1)]
    # outputStack期望出栈序列
    outputStack = []
    output = raw_input()
    output = output.split()
    for i in output:
        outputStack.append(int(i))
    count = 0
    for i in trains:
        if (i != outputStack[count]):
            s.push(i)
        else:
            count += 1
            while (s.size() != 0 and s.top() == outputStack[count]):
                count += 1
                s.pop()
    if (s.size() == 0):
        print "Yes"
    else:
        print "No"
