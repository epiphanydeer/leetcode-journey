# 1371. 每个元音包含偶数次的最长子字符串
'''
给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
