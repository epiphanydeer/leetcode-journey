# 1354. 多次求和构造目标数组
'''
给你一个整数数组 target 。一开始，你有一个数组 A ，它的所有元素均为 1 ，你可以执行以下操作：

 令 x 为你数组里所有元素的和

 选择满足 0 <= i < target.size 的任意下标 i ，并让 A 数组里下标为 i 处的值为 x 。

 你可以重复该过程任意次

如果能从 A 开始构造出目标数组 target ，请你返回 True ，否则返回 False 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
