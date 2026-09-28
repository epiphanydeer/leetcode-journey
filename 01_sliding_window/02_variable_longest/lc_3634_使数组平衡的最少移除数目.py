# 3634. 使数组平衡的最少移除数目
"""
给你一个整数数组 nums 和一个整数 k。
如果一个数组的 最大 元素的值 至多 是其 最小 元素的 k 倍，则该数组被称为是 平衡 的。
你可以从 nums 中移除 任意 数量的元素，但不能使其变为 空 数组。
返回为了使剩余数组平衡，需要移除的元素的 最小 数量。
注意：大小为 1 的数组被认为是平衡的，因为其最大值和最小值相等，且条件总是成立。
示例 1:
输入：nums = [2,1,5], k = 2
输出：1
解释：
 移除 nums[2] = 5 得到 nums = [2, 1]。
 现在 max = 2, min = 1，且 max <= min * k，因为 2 <= 1 * 2。因此，答案是 1。
示例 2:
输入：nums = [1,6,2,9], k = 3
输出：2
解释：
 移除 nums[0] = 1 和 nums[3] = 9 得到 nums = [6, 2]。
 现在 max = 6, min = 2，且 max <= min * k，因为 6 <= 2 * 3。因此，答案是 2。
示例 3:
输入：nums = [4,6], k = 2
输出：0
解释：
 由于 nums 已经平衡，因为 6 <= 4 * 2，所以不需要移除任何元素。
 【解题思路】
 1. 数组最大的数最多只能是最小元素的k倍，不能是k+1倍
 2. 移除最小的数量，因为是最大元素和最小元素，所以是滑窗
 3. 想法是sort排序一下，然后找最小元素的k倍
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def minRemoval(self, nums: List[int], k: int) -> int:
        left, ans = 0, 0
        nums.sort()
        for right, j in enumerate(nums):
            while nums[left] * k < j:
                left += 1
            ans = max(ans, right - left + 1)
        return len(nums) - ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.minRemoval(nums=[2, 1, 5], k=2))
