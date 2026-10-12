# 面试题 17.05.  字母与数字
'''
给定一个放有字母和数字的数组，找到最长的子数组，且包含的字母和数字的个数相同。

返回该子数组，若存在多个最长子数组，返回左端点下标值最小的子数组。若不存在这样的数组，返回一个空数组。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def findLongestSubarray(self, array):
        """
        :type array: List[str]
        :rtype: List[str]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
