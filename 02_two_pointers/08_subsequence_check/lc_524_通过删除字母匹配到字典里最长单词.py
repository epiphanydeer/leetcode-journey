# 524. 通过删除字母匹配到字典里最长单词
'''
给你一个字符串 s 和一个字符串数组 dictionary ，找出并返回 dictionary 中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。

如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
