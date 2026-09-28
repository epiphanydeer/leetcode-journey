# 1081. 不同字符的最小子序列
'''
返回 s 字典序最小的子序列，该子序列包含 s 的所有不同字符，且只包含一次。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
