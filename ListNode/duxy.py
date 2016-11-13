# -*- coding: utf-8 -*-
class Node():
    def __init__(self, val, nt=None):
        self.value = val
        self.next = nt


class ListNode():
    def __init__(self):
        self.headNode = Node(None, None)
        self.headNode.next = self.headNode
        self.head = self.headNode
        self.size = 1

    def add(self, value):
        elementNode = Node(value, None)
        if self.head.value == None:
            elementNode.next = self.headNode
            self.head.next = elementNode
            self.head = elementNode
            self.size += 1
        else:
            elementNode.next = self.head.next
            self.head.next = elementNode
            self.head = elementNode
            self.size += 1

    def delete(self):
        t = self.head
        if self.head.next.value == None:
            self.head = self.head.next
        p = self.head.next
        self.head.next = p.next
        self.head = t
        s.size -= 1

    def NodeNext(self):
        self.head = self.head.next
        if self.head.value == None:
            self.head = self.head.next
s = ListNode()
step = input()
string = raw_input()
for i in string:
    s.add(i)
count = 0
if step != 0:
    choice = raw_input()
    choice = list(choice)
    while count < step:
        if choice[0] == "1":
            s.add(choice[2])
        elif choice[0] == "2":
            s.delete()
        elif choice[0] == "3":
            s.NodeNext()
        count += 1
        if count < step:
            choice = raw_input()
            choice = list(choice)
str = ''
for i in xrange(s.size):
    if s.head.value != None:
        str += s.head.value
    s.head = s.head.next
print str
