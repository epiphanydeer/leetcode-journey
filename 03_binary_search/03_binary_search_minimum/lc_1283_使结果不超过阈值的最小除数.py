# 1283. 使结果不超过阈值的最小除数
"""
给你一个整数数组 nums 和一个正整数 threshold  ，你需要选择一个正整数作为除数，然后将数组里每个数都除以它，并对除法结果求和。

请你找出能够使上述结果小于等于阈值 threshold 的除数中 最小 的那个。

每个数除以除数后都向上取整，比方说 7/3 = 3 ， 10/2 = 5 。

题目保证一定有解。
【解题思路】
1. 因为选择数字越大，和越小，前期不满足，后期满足，单调性，可以二分答案
2. 向上取整，所以用(mid + i - 1) // mid 避免浮点精度
3. left可以取1，right取数组最大值
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """

        def check(mid: int) -> bool:
            total = 0
            for i in nums:
                total += (mid + i - 1) // mid
            return total <= threshold

        left, right = 1, max(nums)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestDivisor(nums=[1, 2, 5, 9], threshold=6))
