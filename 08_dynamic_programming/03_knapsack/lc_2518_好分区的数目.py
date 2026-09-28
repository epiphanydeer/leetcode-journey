# 2518. 好分区的数目
'''
给你一个正整数数组 nums 和一个整数 k 。

分区 的定义是：将数组划分成两个有序的 组 ，并满足每个元素 恰好 存在于 某一个 组中。如果分区中每个组的元素和都大于等于 k ，则认为分区是一个好分区。

返回 不同 的好分区的数目。由于答案可能很大，请返回对 109 + 7 取余 后的结果。

如果在两个分区中，存在某个元素 nums[i] 被分在不同的组中，则认为这两个分区不同。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countPartitions(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
