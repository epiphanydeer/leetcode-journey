# 2574. 左右元素和的差值
'''
给你一个下标从 0 开始的长度为 n 的整数数组 nums。

定义两个数组 leftSum 和 rightSum，其中：

 leftSum[i] 是数组 nums 中下标 i 左侧元素之和。如果不存在对应的元素，leftSum[i] = 0 。

 rightSum[i] 是数组 nums 中下标 i 右侧元素之和。如果不存在对应的元素，rightSum[i] = 0 。

返回长度为 n 数组 answer，其中 answer[i] = |leftSum[i] - rightSum[i]|。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
