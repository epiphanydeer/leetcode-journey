# 1830. 使字符串有序的最少操作次数
'''
给你一个字符串 s （下标从 0 开始）。你需要对 s 执行以下操作直到它变为一个有序字符串：

 找到 最大下标 i ，使得 1 <= i < s.length 且 s[i] < s[i - 1] 。

 找到 最大下标 j ，使得 i <= j < s.length 且对于所有在闭区间 [i, j] 之间的 k 都有 s[k] < s[i - 1] 。

 交换下标为 i - 1​​​​ 和 j​​​​ 处的两个字符。

 将下标 i 开始的字符串后缀反转。

请你返回将字符串变成有序的最少操作次数。由于答案可能会很大，请返回它对 109 + 7 取余 的结果。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def makeStringSorted(self, s):
        """
        :type s: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
