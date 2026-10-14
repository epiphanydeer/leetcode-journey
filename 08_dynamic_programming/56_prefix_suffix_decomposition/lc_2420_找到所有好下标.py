# 2420. 找到所有好下标
'''
给你一个大小为 n 下标从 0 开始的整数数组 nums 和一个正整数 k 。

对于 k <= i < n - k 之间的一个下标 i ，如果它满足以下条件，我们就称它为一个 好 下标：

 下标 i 之前 的 k 个元素是 非递增的 。

 下标 i 之后 的 k 个元素是 非递减的 。

按 升序 返回所有好下标。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def goodIndices(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
