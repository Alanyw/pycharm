# -*- coding: utf-8 -*-

temp = raw_input()
temp = temp.split()
magic = int(temp[0])
count = int(temp[1])
magic_name = raw_input()
magic_name = magic_name.split()
magic_hurt = raw_input()
magic_hurt = magic_hurt.split()
step = 0
magic_dict = {}
for i in xrange(len(magic_hurt)):
    magic_dict[magic_name[i]] = magic_hurt[i]
while step < count:
    operation = raw_input()
    operation = operation.split()
    if int(operation[0]) == 1:
        if operation[1] in magic_dict:
            print magic_dict[operation[1]]
        else:
            print "what?"
    if int(operation[0]) == 2:
        magic_dict[operation[1]] = operation[2]
    step += 1
