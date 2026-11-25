# 3152. 特殊数组 II
"""
如果数组的每一对相邻元素都是两个奇偶性不同的数字，则该数组被认为是一个 特殊数组 。

你有一个整数数组 nums 和一个二维整数矩阵 queries，对于 queries[i] = [fromi, toi]，请你帮助你检查 子数组 nums[fromi..toi] 是不是一个 特殊数组 。

返回布尔数组 answer，如果 nums[fromi..toi] 是特殊数组，则 answer[i] 为 true ，否则，answer[i] 为 false 。
【解题思路】
1. 检查奇偶性，找断点，看差值是否为0
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def isArraySpecial(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        s = [0] * len(nums)
        for idx, x in enumerate(nums[1:], 1):
            if x % 2 == nums[idx - 1] % 2:
                s[idx] += s[idx - 1] + 1
            else:
                s[idx] += s[idx - 1]
        ans = []
        for l, r in queries:
            ans.append(s[r] - s[l] == 0)
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.isArraySpecial(nums=[3, 4, 1, 2, 6], queries=[[0, 4]]))
    print(solution.isArraySpecial(nums=[4, 3, 1, 6], queries=[[0, 2], [2, 3]]))
