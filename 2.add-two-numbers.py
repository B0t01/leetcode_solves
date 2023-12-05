#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        d = ListNode(0)
        cu = d
        ca = 0
        while ca or l1 or l2:
            if l1:
                ca+=l1.val
                l1=l1.next
            if l2:
                ca+=l2.val
                l2.next
            cu.next = ListNode(ca%10)
            ca//=10
            cu=cu.next
        return d.next

# @lc code=end

