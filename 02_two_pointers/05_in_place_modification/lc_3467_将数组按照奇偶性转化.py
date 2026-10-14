# 3467. 将数组按照奇偶性转化
"""
给你一个整数数组 nums。请你按照以下顺序 依次 执行操作，转换 nums：
 将每个偶数替换为 0。
 将每个奇数替换为 1。
 按 非递减 顺序排序修改后的数组。
执行完这些操作后，返回结果数组。
示例 1:
输入：nums = [4,3,2,1]
输出：[0,0,1,1]
解释：

 将偶数（4 和 2）替换为 0，将奇数（3 和 1）替换为 1。现在，nums = [0, 1, 0, 1]。

 按非递减顺序排序 nums，得到 nums = [0, 0, 1, 1]。
 【解题思路】
 1. 也是依次执行的，先把奇偶数换成10，然后排序
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            if i % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        left, right = 0, 0
        while right < n:
            if nums[right] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        return nums


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.transformArray(nums=[4, 3, 2, 1]))
