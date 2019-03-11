#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (33.04%)
# Total Accepted:    416.2K
# Total Submissions: 1.3M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        strs.sort(key = lambda i:len(i))
        _resultList = None
        for index in xrange(len(strs)):
            _charList = map(str, strs[index])
            if _resultList == None:
                _resultList = _charList
                continue
            
            for x in xrange(len(_resultList)):
                if _charList[x] != _resultList[x]:
                    _resultList = _resultList[:x:]
                    break
        
        return ''.join(_resultList)

