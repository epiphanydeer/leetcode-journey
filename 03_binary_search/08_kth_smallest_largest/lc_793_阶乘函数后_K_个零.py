# 793. 阶乘函数后 K 个零
'''
f(x) 是 x! 末尾是 0 的数量。回想一下 x! = 1 * 2 * 3 * ... * x，且 0! = 1 。

 例如， f(3) = 0 ，因为 3! = 6 的末尾没有 0 ；而 f(11) = 2 ，因为 11!= 39916800 末端有 2 个 0 。

给定 k，找出返回能满足 f(x) = k 的非负整数 x 的数量。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def preimageSizeFZF(self, k):
        """
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
