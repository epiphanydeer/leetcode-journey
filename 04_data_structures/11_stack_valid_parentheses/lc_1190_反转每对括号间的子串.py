# 1190. 反转每对括号间的子串
'''
给出一个字符串 s（仅含有小写英文字母和括号）。

请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。

注意，您的结果中 不应 包含任何括号。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
