# 1802. 有界数组中指定下标处的最大值
'''
给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：

 nums.length == n

 nums[i] 是 正整数 ，其中 0 <= i < n

 abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1

 nums 中所有元素之和不超过 maxSum

 nums[index] 的值被 最大化

返回你所构造的数组中的 nums[index] 。

注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
