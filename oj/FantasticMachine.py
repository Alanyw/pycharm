# -*- coding: utf-8 -*-
class stringInput:
    def __init__(self):
        self.items = []
        self.nextPos = 0

    def size(self):
        return len(self.items)


string = []
s = stringInput()
step = input()
init_string = raw_input()
s.items = list(init_string)
s.nextPos = len(s.items)
count = 0
while count < step:
    string_input = raw_input()
    string_input = list(string_input)
    if string_input[0] == '1':
        if s.nextPos > s.size():
            s.nextPos -= s.size()
        s.items.insert(s.nextPos, string_input[2])
        s.nextPos += 1
        if s.nextPos > s.size():
            s.nextPos -= s.size()
    if string_input[0] == '2':
        if s.nextPos >= s.size():
            s.nextPos -= s.size()
            s.items.pop(s.nextPos)
        else:
            s.items.pop(s.nextPos)
    if string_input[0] == '3':
        if s.nextPos > s.size():
            s.nextPos -= s.size()
            s.nextPos += 1
        s.nextPos += 1
    if s.nextPos > s.size():
        s.nextPos -= s.size()
    string_input = []
    count += 1
out = ''
for i in xrange(len(s.items)):
    out += str(s.items[s.nextPos-1])
    s.nextPos+=1
    if s.nextPos > s.size():
        s.nextPos -= s.size()
print out