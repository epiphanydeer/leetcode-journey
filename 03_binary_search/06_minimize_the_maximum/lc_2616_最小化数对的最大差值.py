# 2616. 最小化数对的最大差值
'''
给你一个下标从 0 开始的整数数组 nums 和一个整数 p 。请你从 nums 中找到 p 个下标对，每个下标对对应数值取差值，你需要使得这 p 个差值的 最大值 最小。同时，你需要确保每个下标在这 p 个下标对中最多出现一次。

对于一个下标对 i 和 j ，这一对的差值为 |nums[i] - nums[j]| ，其中 |x| 表示 x 的 绝对值 。

请你返回 p 个下标对对应数值 最大差值 的 最小值 。我们定义空集的最大值为零。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
