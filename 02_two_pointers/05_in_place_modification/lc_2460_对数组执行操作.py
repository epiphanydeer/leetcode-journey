# 2460. 对数组执行操作
"""
给你一个下标从 0 开始的数组 nums ，数组大小为 n ，且由 非负 整数组成。
你需要对数组执行 n - 1 步操作，其中第 i 步操作（从 0 开始计数）要求对 nums 中第 i 个元素执行下述指令：
 如果 nums[i] == nums[i + 1] ，则 nums[i] 的值变成原来的 2 倍，nums[i + 1] 的值变成 0 。否则，跳过这步操作。
在执行完 全部 操作后，将所有 0 移动 到数组的 末尾 。
 例如，数组 [1,0,2,0,0,1] 将所有 0 移动到末尾后变为 [1,2,1,0,0,0] 。
返回结果数组。
注意 操作应当 依次有序 执行，而不是一次性全部执行。
【解题思路】
1. 要依次执行，先确定如果当前序列和下一个序列相等就二倍，然后下一个数字变0
2. 然后再把0移到最后
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                nums[left] = nums[left] * 2
                nums[right] = 0
            left += 1
            right += 1
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return nums


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.applyOperations(nums=[1, 2, 2, 1, 1, 0]))
