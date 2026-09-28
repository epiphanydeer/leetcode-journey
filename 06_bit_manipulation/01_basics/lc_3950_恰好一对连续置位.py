# 3950. 恰好一对连续置位
'''
给你一个整数 n 。

如果其二进制表示中 恰好 仅包含 一对 相邻的置位 ，则返回 true ，否则返回 false 。

整数中的 置位 是指其 二进制 表示中的 1 。

 

示例 1：

输入： n = 6

输出： true

解释：

 6 的二进制表示为 110 。

 恰好存在一对相邻的置位（"11"）。因此，答案为 true 。

示例 2：

输入： n = 5

输出： false

解释：

 5 的二进制表示为 101 。

 不存在相邻的置位。因此，答案为 false 。

 

提示：

 0 <= n <= 105
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def consecutiveSetBits(self, n):
        """
        :type n: int
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
