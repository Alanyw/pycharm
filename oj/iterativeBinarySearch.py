#!/usr/bin/python
# -*- coding: utf-8 -*-
def iterativeBinarySearch(items, target):
    first = 0
    last = len(items) - 1

    while first <= last:
        middle = (first + last) // 2
        if target == items[middle]:
            return middle
        elif target < items[middle]:
            last = middle - 1
        else:
            first = middle + 1

    return False
nums_times = raw_input()
nums_times = nums_times.split( )
nums_times = list(nums_times)
times = nums_times[1]
input_list = raw_input()
input_list = input_list.split( )
input_list = list(input_list)
list_input=[]
for i in input_list:
    list_input.append(int(i))
count = 0
while count < times:
    nums = input()
    if iterativeBinarySearch(list_input,nums) is False:
        print "-1"
    else:
        print iterativeBinarySearch(list_input,nums)
    count += 1
    