# 2163. 删除元素后和的最小差值
'''
给你一个下标从 0 开始的整数数组 nums ，它包含 3 * n 个元素。

你可以从 nums 中删除 恰好 n 个元素，剩下的 2 * n 个元素将会被分成两个 相同大小 的部分。

 前面 n 个元素属于第一部分，它们的和记为 sumfirst 。

 后面 n 个元素属于第二部分，它们的和记为 sumsecond 。

两部分和的 差值 记为 sumfirst - sumsecond 。

 比方说，sumfirst = 3 且 sumsecond = 2 ，它们的差值为 1 。

 再比方，sumfirst = 2 且 sumsecond = 3 ，它们的差值为 -1 。

请你返回删除 n 个元素之后，剩下两部分和的 差值的最小值 是多少。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
