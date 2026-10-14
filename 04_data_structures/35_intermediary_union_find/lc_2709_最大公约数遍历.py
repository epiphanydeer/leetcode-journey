# 2709. 最大公约数遍历
'''
给你一个下标从 0 开始的整数数组 nums ，你可以在一些下标之间遍历。对于两个下标 i 和 j（i != j），当且仅当 gcd(nums[i], nums[j]) > 1 时，我们可以在两个下标之间通行，其中 gcd 是两个数的 最大公约数 。

你需要判断 nums 数组中 任意 两个满足 i < j 的下标 i 和 j ，是否存在若干次通行可以从 i 遍历到 j 。

如果任意满足条件的下标对都可以遍历，那么返回 true ，否则返回 false 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def canTraverseAllPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
