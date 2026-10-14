# 2659. 将数组清空
'''
给你一个包含若干 互不相同 整数的数组 nums ，你需要执行以下操作 直到数组为空 ：

 如果数组中第一个元素是当前数组中的 最小值 ，则删除它。

 否则，将第一个元素移动到数组的 末尾 。

请你返回需要多少个操作使 nums 为空。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countOperationsToEmptyArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
