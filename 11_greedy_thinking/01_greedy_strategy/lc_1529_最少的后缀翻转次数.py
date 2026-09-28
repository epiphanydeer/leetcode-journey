# 1529. 最少的后缀翻转次数
'''
给你一个长度为 n 、下标从 0 开始的二进制字符串 target 。你自己有另一个长度为 n 的二进制字符串 s ，最初每一位上都是 0 。你想要让 s 和 target 相等。

在一步操作，你可以选择下标 i（0 <= i < n）并翻转在 闭区间 [i, n - 1] 内的所有位。翻转意味着 '0' 变为 '1' ，而 '1' 变为 '0' 。

返回使 s 与 target 相等需要的最少翻转次数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
