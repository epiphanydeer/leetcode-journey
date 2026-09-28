# 2384. 最大回文数字
'''
给你一个仅由数字（0 - 9）组成的字符串 num 。

请你找出能够使用 num 中数字形成的 最大回文 整数，并以字符串形式返回。该整数不含 前导零 。

注意：

 你 无需 使用 num 中的所有数字，但你必须使用 至少 一个数字。

 数字可以重新排序。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def largestPalindromic(self, num):
        """
        :type num: str
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
