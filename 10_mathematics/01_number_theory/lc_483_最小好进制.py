# 483. 最小好进制
'''
以字符串的形式给出 n , 以字符串的形式返回 n 的最小 好进制  。

如果 n 的  k(k>=2) 进制数的所有数位全为1，则称 k(k>=2) 是 n 的一个 好进制 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
