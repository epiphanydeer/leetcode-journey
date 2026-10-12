# 18. 四数之和
"""
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
 0 <= a, b, c, d < n
 a、b、c 和 d 互不相同
 nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。
【解题思路】
1. 四个数，需要固定两个数，那就俩三数之和的嵌套
2. 单调性判断：当移动某个指针导致状态发生改变后，先前被排除掉的元素，
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
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    x = nums[i] + nums[j] + nums[left] + nums[right]
                    if x > target:
                        right -= 1
                    elif x < target:
                        left += 1
                    if x == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
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
    print(solution.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
