# 2134. 最少交换次数来组合所有的 1 II
'''
交换 定义为选中一个数组中的两个 互不相同 的位置并交换二者的值。

环形 数组是一个数组，可以认为 第一个 元素和 最后一个 元素 相邻 。

给你一个 二进制环形 数组 nums ，返回在 任意位置 将数组中的所有 1 聚集在一起需要的最少交换次数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
