# 16. 最接近的三数之和
"""
给定一个长度为 n 的整数数组 nums 和 一个整数 target。

请你从 nums 中选出三个在 不同下标位置 的整数，使它们的和与 target 最接近。

返回这三个数的和。

假定每组输入只存在 恰好 一个解。
【解题思路】
1. 固定一个元素，剩下俩元素用双指针去遍历
2. 接近，就是看ans 和 目前数字之间的距离（绝对值）
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
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = inf
        n = len(nums)
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                x = nums[i] + nums[left] + nums[right]
                if abs(x - target) < abs(ans - target):
                    ans = x
                if x > target:
                    right -= 1
                else:
                    left += 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSumClosest(nums=[0, 0, 0], target=1))
