# 2521. 数组乘积中的不同质因数数目
'''
给你一个正整数数组 nums ，对 nums 所有元素求积之后，找出并返回乘积中 不同质因数 的数目。

注意：

 质数 是指大于 1 且仅能被 1 及自身整除的数字。

 如果 val2 / val1 是一个整数，则整数 val1 是另一个整数 val2 的一个因数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def distinctPrimeFactors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
