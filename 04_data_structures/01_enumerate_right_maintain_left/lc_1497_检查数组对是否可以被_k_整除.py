# 1497. 检查数组对是否可以被 k 整除
'''
给你一个整数数组 arr 和一个整数 k ，其中数组长度是偶数，值为 n 。

现在需要把数组恰好分成 n / 2 对，以使每对数字的和都能够被 k 整除。

如果存在这样的分法，请返回 true ；否则，返回 false。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
