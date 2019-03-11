#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (46.01%)
# Total Accepted:    520.9K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
#
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
        resultList = []
        while True:
            if l1 != None:
                resultList.append(l1.val)
                l1 = l1.next
            
            if l2 != None:
                resultList.append(l2.val)
                l2 = l2.next
            
            if l1 == None and l2 == None:
                break
        
        # print(sorted(resultList))
        return self.ListToListNode(sorted(resultList))

    def ListToListNode(self, listVar):
        result = None
        reverse_list = listVar[::-1]
        for i in xrange(len(reverse_list)):
            if i == 0:
                result = ListNode(reverse_list[i])
                continue
            tempNode = ListNode(reverse_list[i])
            tempNode.next = result
            result = tempNode
        return result
        

