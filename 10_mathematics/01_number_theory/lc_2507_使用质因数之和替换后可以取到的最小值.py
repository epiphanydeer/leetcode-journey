# 2507. 使用质因数之和替换后可以取到的最小值
'''
给你一个正整数 n 。

请你将 n 的值替换为 n 的 质因数 之和，重复这一过程。

 注意，如果 n 能够被某个质因数多次整除，则在求和时，应当包含这个质因数同样次数。

返回 n 可以取到的最小值。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def smallestValue(self, n):
        """
        :type n: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
