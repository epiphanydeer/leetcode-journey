# 1362. 最接近的因数
'''
给你一个整数 num，请你找出同时满足下面全部要求的两个整数：

 两数乘积等于  num + 1 或 num + 2

 以绝对差进行度量，两数大小最接近

你可以按任意顺序返回这两个整数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
