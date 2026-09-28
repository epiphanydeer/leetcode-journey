# 360. 有序转化数组
'''
给你一个已经排好序的整数数组 nums 和整数 a、b、c。对于数组中的每一个元素 nums[i]，计算函数值 f(x) = ax² + bx + c，请按升序返回数组。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
