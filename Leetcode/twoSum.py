# -*- coding: utf-8 -*-
from pip._vendor.requests.packages.urllib3.connectionpool import xrange


class Solution:
    # 使用数组
    def twoSum(self, num, target):
        index = []
        num_to_sum = num[:]
        num_to_sum.sort()
        i = 0;
        j = len(num_to_sum) - 1
        # 同时从数组两头开始找
        while i < j:
            if num_to_sum[i] + num_to_sum[j] == target:
                # 从前往后找
                for k in range(0, len(num)):
                    if num[k] == num_to_sum[i]:
                        index.append(k)
                        break
                # 从后往前走
                # range(len(num)-1,-1,-1)表示从len(num)开始倒序输出
                for k in range(len(num) - 1, -1, -1):
                    if num[k] == num_to_sum[j]:
                        index.append(k)
                        break
                index.sort()
                break
            elif num_to_sum[i] + num_to_sum[j] < target:
                i += 1
            elif num_to_sum[i] + num_to_sum[j] > target:
                j -= 1

        return (index[0], index[1])

    # 使用dict方法
    def twoSum_(self, num, target):
        dict = {}
        for i in xrange(len(num)):
            x = num[i]
            if target - x in dict:
                return (dict[target - x], i)
            dict[x] = i
        return 0
