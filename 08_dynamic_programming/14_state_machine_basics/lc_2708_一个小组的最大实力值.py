# 2708. 一个小组的最大实力值
'''
给你一个下标从 0 开始的整数数组 nums ，它表示一个班级中所有学生在一次考试中的成绩。老师想选出一部分同学组成一个 非空 小组，且这个小组的 实力值 最大，如果这个小组里的学生下标为 i0, i1, i2, ... , ik ，那么这个小组的实力值定义为 nums[i0] * nums[i1] * nums[i2] * ... * nums[ik​] 。

请你返回老师创建的小组能得到的最大实力值为多少。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maxStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
