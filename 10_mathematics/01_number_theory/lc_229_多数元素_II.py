# 229. 多数元素 II
'''
给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊n / 3⌋ 次的元素。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
