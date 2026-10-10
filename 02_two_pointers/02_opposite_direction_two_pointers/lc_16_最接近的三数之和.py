# 16. 最接近的三数之和
"""
给定一个长度为 n 的整数数组 nums 和 一个整数 target。

请你从 nums 中选出三个在 不同下标位置 的整数，使它们的和与 target 最接近。

返回这三个数的和。

假定每组输入只存在 恰好 一个解。
【解题思路】
1. 固定第一个数，然后俩指针分别从右边第一个和最后一个开始遍历，
参考之前的方法，排序，比大小，大了就缩小右指针，反之同理。
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = inf
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                x = nums[i] + nums[left] + nums[right]
                if x == target:
                    return target
                if abs(x - target) < abs(target - ans):
                    ans = x
                if x > target:
                    right -= 1
                else:
                    left += 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSumClosest(nums=[-1, 2, 1, -4], target=1))
