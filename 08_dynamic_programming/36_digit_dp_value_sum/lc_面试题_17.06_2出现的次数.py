# 面试题 17.06. 2出现的次数
'''
编写一个方法，计算从 0 到 n (含 n) 中数字 2 出现的次数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def numberOf2sInRange(self, n):
        """
        :type n: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
