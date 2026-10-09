# 15. 三数之和
"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
【解题思路】
1. 与16题类似，但是要注意重复的情况，要先排除排头的重复，还要排除左右指针的重复
2. 排序，定开头，左右指针移动，并且判断重复
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                x = nums[i] + nums[left] + nums[right]
                if x > 0:
                    right -= 1
                elif x < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    if nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    if nums[right] == nums[right + 1]:
                        right -= 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum(nums=[0, 0, 0]))
