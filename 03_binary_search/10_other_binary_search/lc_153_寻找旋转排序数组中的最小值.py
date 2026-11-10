# 153. 寻找旋转排序数组中的最小值
"""
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：

 若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]

 若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]

注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
【解题思路】
1. 和最后一个数字比较，两种情况，如果大于它，说明Mid在另一段，小于说明在同一段
2. 因此大于它了，那就left挪到mid+1，
3. 因为比较的是定值，所以不合格的会回退
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.findMin(nums=[3, 4, 5, 1, 2]))
    print(solution.findMin(nums=[4, 5, 6, 7, 0, 1, 2]))
