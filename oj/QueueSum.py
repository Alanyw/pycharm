from collections import deque

count = input()
step = 0
while step < count:
    numsAndOpe = raw_input()
    numsAndOpe = numsAndOpe.split()
    nums = raw_input()
    nums = nums.split()
    j = 0
    nums = [int(i) for i in nums]
    nums = deque(nums)
    numsNew = deque()
    for i in xrange(int(numsAndOpe[1])):
        numsNew.append(nums.popleft())
    sums = sum(numsNew)
    print sums % 1000000007
    for i in xrange(len(nums)):
        numsNew.append(nums.popleft())
        sums = sums - numsNew.popleft() + numsNew[-1]
        print sums % 1000000007
    step += 1
