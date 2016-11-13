# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = ListNode(0)
        p = head
        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) / 10
            l1 = l1.next
            l2 = l2.next
            p = p.next
        # 两个链表长度不一样时,为以下处理方法

        # l1比l2长
        if l1:
            while l1:
                p.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) / 10
                l1 = l1.next
                p = p.next
        # l2比l1长
        if l2:
            while l2:
                p.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) / 10
                l2 = l2.next
                p = p.next
                # 当最大位大于9时,即carry大于9,还需要进一位
        if carry == 1:
            p.next = ListNode(1)
        return head.next


hello = Solution
p1 = [2, 4, 3]
l1 = ListNode(p1)
p2 = [5, 6, 4]
l2 = ListNode(p2)
print type(l1)
print l1.val
hello.addTwoNumbers(l1, l2)
