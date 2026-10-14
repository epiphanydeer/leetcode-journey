# 397. 整数替换
'''
给定一个正整数 n ，你可以做如下操作：

 如果 n 是偶数，则用 n / 2替换 n 。

 如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。

返回 n 变为 1 所需的 最小替换次数 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
