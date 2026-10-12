# 15. 三数之和
"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
【解题思路】
1. 固定一个元素，剩下俩元素用双指针去遍历
2. 还是同样的搜索空间，排序后，如果最小的加上最大的都小，那直接跳过这个left，
    如果最小的和最大的加起来都很大了，那就要跳过right了
3. 单调性判断：当移动某个指针导致状态发生改变后，先前被排除掉的元素，
有没有可能在后面的轮次里重新变成合法解？ 没有
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n - 2):
            left, right = i + 1, n - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                x = nums[i] + nums[left] + nums[right]
                if x > 0:
                    right -= 1
                elif x < 0:
                    left += 1
                if x == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum(nums=[0, 1, 1]))
