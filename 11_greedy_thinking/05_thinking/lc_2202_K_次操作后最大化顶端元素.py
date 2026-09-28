# 2202. K 次操作后最大化顶端元素
'''
给你一个下标从 0 开始的整数数组 nums ，它表示一个 堆 ，其中 nums[0] 是堆顶的元素。

每一次操作中，你可以执行以下操作 之一 ：

 如果堆非空，那么 删除 堆顶端的元素。

 如果存在 1 个或者多个被删除的元素，你可以从它们中选择任何一个，添加 回堆顶，这个元素成为新的堆顶元素。

同时给你一个整数 k ，它表示你总共需要执行操作的次数。

请你返回 恰好 执行 k 次操作以后，堆顶元素的 最大值 。如果执行完 k 次操作以后，堆一定为空，请你返回 -1 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maximumTop(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
