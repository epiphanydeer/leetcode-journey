# 2524. 子数组的最大频率分数
'''
给定一个整数数组 nums 和一个正整数 k。

数组的频率得分是数组中不同值的幂次之和，并将和对 10^9 + 7 取模。

例如，数组 [5,4,5,7,4,4] 的频率得分为 (4^3 + 5^2 + 7^1) modulo (10^9 + 7) = 96。

返回 nums 中长度为 k 的子数组的最大频率得分。你需要返回取模后的最大值，而不是实际值。

子数组是一个数组的连续部分。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maxFrequencyScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
