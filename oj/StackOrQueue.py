# -*- coding: utf-8 -*-
import copy


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

    def printOut(self):
        p = copy.deepcopy(self)
        stackStr = ""
        while not p.empty():
            stackStr += str(p.pop())
        return stackStr


class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, items):
        self.items.append(items)

    def dequeue(self):
        return self.items.pop(0)

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def printOut(self):
        p = copy.deepcopy(self)
        queueStr = ''
        while not p.empty():
            queueStr += str(p.dequeue())
        return queueStr

    def clear(self):
        del self.items[:]


step = input()
count = 0
judge = []
result = []
s = Stack()
q = Queue()
while count < step:
    stringLen = input()
    string = raw_input()
    string = string.split()
    stringOut = raw_input()
    stringOut = stringOut.split()
    stringOut = "".join(stringOut)
    for i in xrange(len(string)):
        s.push(string[i])
        q.enqueue(string[i])
    if s.printOut() == stringOut:
        judge.append('stack')
    if q.printOut() == stringOut:
        judge.append('queue')
    strJudge = ''
    strJudge = "".join(judge)
    if strJudge == 'stackqueue':
        result.append('both')
    elif strJudge == 'stack':
        result.append('stack')
    elif strJudge == 'queue':
        result.append('queue')
    elif strJudge == '':
        result.append('neither')
    print "".join(result)
    del result[:],
    del judge[:]
    count += 1
    s.clear()
    q.clear()
