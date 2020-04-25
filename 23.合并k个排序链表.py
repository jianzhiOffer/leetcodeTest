#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (49.62%)
# Likes:    581
# Dislikes: 0
# Total Accepted:    100K
# Total Submissions: 199.7K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 
# 示例:
# 
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def mergeTwoLists(l1, l2):
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

class Solution(object):
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 暴力递归 会超时 时间复杂度O(NM)
        # minL = None
        # newList = []
        # for l in lists:
        #     if l is None:
        #         continue
        #     if minL is None:
        #         minL = l
        #     else:
        #         if minL.val > l.val:
        #             newList.append(minL)
        #             minL = l
        #         else:
        #             newList.append(l)
        # if minL:
        #     newList.append(minL.next)
        #     minL.next = Solution().mergeKLists(newList)
        # return minL
    
        # 运用归并递归 不会超时 时间复杂度O(NlogN)
        if not lists:
            return
        length = len(lists)
        newList = []
        for i in xrange(0, length, 2):
            if i == length - 1:
                newList.append(lists[i])
            else:
                newList.append(mergeTwoLists(*lists[i:i+2]))
        if len(newList) == 1:
            return newList[0]
        return Solution().mergeKLists(newList)
            
            
# @lc code=end

