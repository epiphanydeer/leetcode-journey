# 2389. 和有限的最长子序列
"""
给你一个长度为 n 的整数数组 nums ，和一个长度为 m 的整数数组 queries 。

返回一个长度为 m 的数组 answer ，其中 answer[i] 是 nums 中 元素之和小于等于 queries[i] 的 子序列 的 最大 长度  。

子序列 是由一个数组删除某些元素（也可以不删除）但不改变剩余元素顺序得到的一个数组。
【解题思路】
1. 就是对应这queries，遍历每个元素，在Nums找小于等于的最大长度
2. 对Nums排序后计算前缀和，然后二分前缀和的新数组
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def lower_bound(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        ans = []
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        for idx, j in enumerate(queries):
            point = self.lower_bound(nums, j)
            ans.append(point)
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.answerQueries(nums=[4, 5, 2, 1], queries=[3, 10, 21]))
    print(solution.answerQueries(nums=[2, 3, 4, 5], queries=[1]))
