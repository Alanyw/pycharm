#!/usr/bin/env python
# encoding: utf-8

def ChangKey(key, m, di):
    key01 = (key + di) % m
    return key01


while 1:
    hashLen = raw_input()
    hashLen = hashLen.split()
    count = int(hashLen[0])
    m = int(hashLen[1])
    table = [0] * m
    dict01 = {}.fromkeys(xrange(m), 0)
    step = 0
    while step < count:
        hashInput = []
        hash_input = raw_input()
        hash_input = hash_input.split()
        for i in hash_input:
            hashInput.append(int(i))
        if hashInput[0] == 1:
            key = hashInput[1] % m
            if dict01[key] != 0:
                NewKey = ChangKey(key, m, 1)
                while dict01[NewKey] != 0:
                    NewKey = ChangKey(NewKey, m, 1)
                dict01[NewKey] = hashInput[1]
            else:
                dict01[key] = hashInput[1]
        if hashInput[0] == 2:
            values = dict01.values()
            value = []
            for i in values:
                value.append("%s"%i)
            print ' '.join(value)
        step += 1
