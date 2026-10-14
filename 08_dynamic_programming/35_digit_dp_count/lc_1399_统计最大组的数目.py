# 1399. 统计最大组的数目
'''
给定一个整数 n 。

我们需要根据数字的数位和将 1 到 n 的数字分组。例如，数字 14 和 5 属于 同一 组，而数字 13 和 3 属于 不同 组。

返回最大组的数字数量，即元素数量 最多 的组。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
