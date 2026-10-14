# 1388. 3n 块披萨
'''
给你一个披萨，它由 3n 块不同大小的部分组成，现在你和你的朋友们需要按照如下规则来分披萨：

 你挑选 任意 一块披萨。

 Alice 将会挑选你所选择的披萨逆时针方向的下一块披萨。

 Bob 将会挑选你所选择的披萨顺时针方向的下一块披萨。

 重复上述过程直到没有披萨剩下。

每一块披萨的大小按顺时针方向由循环数组 slices 表示。

请你返回你可以获得的披萨大小总和的最大值。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maxSizeSlices(self, slices):
        """
        :type slices: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
