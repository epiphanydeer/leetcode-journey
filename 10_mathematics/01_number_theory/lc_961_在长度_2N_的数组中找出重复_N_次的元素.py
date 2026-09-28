# 961. 在长度 2N 的数组中找出重复 N 次的元素
'''
给你一个整数数组 nums ，该数组具有以下属性：

 nums.length == 2 * n.

 nums 包含 n + 1 个 不同的 元素，其中 n 个值在数组中出现 恰好一次。

 nums 中恰有一个元素重复 n 次

找出并返回重复了 n 次的那个元素。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
