#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (60.62%)
# Likes:    965
# Dislikes: 0
# Total Accepted:    235.9K
# Total Submissions: 385.6K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 递归
        # if l1 is None:
        #     return l2
        # if l2 is None:
        #     return l1
        # l1, l2 = (l1, l2) if l1.val < l2.val else (l2, l1)
        # l1.next = Solution().mergeTwoLists(l1.next, l2)
        # return l1
    
        # 非递归
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        dummy = node = ListNode(0)
        while l1 and l2:
            l1, l2 = (l1, l2) if l1.val < l2.val else (l2, l1)
            node.next = l1
            node = node.next
            l1 = l1.next
        node.next = l1 if l1 else l2
        return dummy.next

        
# @lc code=end

