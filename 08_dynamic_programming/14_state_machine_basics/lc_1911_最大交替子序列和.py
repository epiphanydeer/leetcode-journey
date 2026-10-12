# 1911. 最大交替子序列和
'''
一个下标从 0 开始的数组的 交替和 定义为 偶数 下标处元素之 和 减去 奇数 下标处元素之 和 。

 比方说，数组 [4,2,5,3] 的交替和为 (4 + 5) - (2 + 3) = 4 。

给你一个数组 nums ，请你返回 nums 中任意子序列的 最大交替和 （子序列的下标 重新 从 0 开始编号）。

一个数组的 子序列 是从原数组中删除一些元素后（也可能一个也不删除）剩余元素不改变顺序组成的数组。比方说，[2,7,4] 是 [4,2,3,7,2,1,4] 的一个子序列（加粗元素），但是 [2,4,2] 不是。

 

示例 1：

输入：nums = [4,2,5,3]
输出：7
解释：最优子序列为 [4,2,5] ，交替和为 (4 + 5) - 2 = 7 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
