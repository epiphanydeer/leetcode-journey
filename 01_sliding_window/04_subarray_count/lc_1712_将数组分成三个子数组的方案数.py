# 1712. 将数组分成三个子数组的方案数
'''
我们称一个分割整数数组的方案是 好的 ，当它满足：

 数组被分成三个 非空 连续子数组，从左至右分别命名为 left ， mid ， right 。

 left 中元素和小于等于 mid 中元素和，mid 中元素和小于等于 right 中元素和。

给你一个 非负 整数数组 nums ，请你返回 好的 分割 nums 方案数目。由于答案可能会很大，请你将结果对 109 + 7 取余后返回。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
