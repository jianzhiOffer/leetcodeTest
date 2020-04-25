# -*- coding:utf-8 -*-
#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (36.96%)
# Likes:    4214
# Dislikes: 0
# Total Accepted:    394.9K
# Total Submissions: 1.1M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 
# 示例：
# 
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#     def __repr__(self):
#         """Returns a visual representation of the node and all its following nodes."""
#         string_rep = ""
#         temp = self
#         while temp:
#             string_rep += "<%s> ---> " % temp.val
#             temp = temp.next
#         string_rep += "<END>"
#         return string_rep

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # if not l1:
        #     return l2
        # if not l2:
        #     return l1
        # if not l1 and not l2:
        #     return
        # head = node = None
        # add = 0
        # while l1 or l2:
        #     sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + add
        #     val, add = sum % 10, sum // 10
        #     newNode = ListNode(val)
        #     if not head:
        #         head = newNode
        #     if node:
        #         node.next = newNode
        #     node = newNode
        #     if l1:
        #         l1 = l1.next
        #     if l2:
        #         l2 = l2.next
        # if add > 0:
        #     node.next = ListNode(add)
        # return head
        carry = 0
        # dummy head
        head = curr = ListNode(0)
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            curr.next = ListNode(val % 10)
            curr = curr.next
            carry = val / 10
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next
# @lc code=end
# if __name__ == "__main__":
#     a = Solution()
#     l1 = n = ListNode(2)
#     n.next = ListNode(4)
#     n = n.next
#     n.next = ListNode(3)
    
#     l2 = n = ListNode(5)
#     n.next = ListNode(6)
#     n = n.next
#     n.next = ListNode(4)

#     print a.addTwoNumbers(l1, l2)
