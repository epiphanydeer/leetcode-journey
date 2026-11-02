# 2367. 等差三元组的数目
"""
给你一个下标从 0 开始、严格递增 的整数数组 nums 和一个正整数 diff 。如果满足下述全部条件，则三元组 (i, j, k) 就是一个 等差三元组 ：
 i < j < k ，
 nums[j] - nums[i] == diff 且
 nums[k] - nums[j] == diff
返回不同 等差三元组 的数目。
【解题思路】
1. 遍历最大值，然后去判断，如果左指针加上diff小于i了，就left+=1，大于了就跳过
右指针加上两倍diff小于i了，就right+=1，大了就跳
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        left, right = 0, 1
        ans = 0
        for i in nums:
            while nums[left] + 2 * diff < i:
                left += 1
            if nums[left] + 2 * diff > i:
                continue
            while nums[right] + diff < i:
                right += 1
            if nums[right] + diff == i:
                ans += 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.arithmeticTriplets(nums=[4, 5, 6, 7, 8, 9], diff=2))
