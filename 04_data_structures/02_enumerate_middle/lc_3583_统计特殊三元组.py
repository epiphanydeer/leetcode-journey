# 3583. 统计特殊三元组
"""
给你一个整数数组 nums。

特殊三元组 定义为满足以下条件的下标三元组 (i, j, k)：

 0 <= i < j < k < n，其中 n = nums.length

 nums[i] == nums[j] * 2

 nums[k] == nums[j] * 2

返回数组中 特殊三元组 的总数。

由于答案可能非常大，请返回结果对 109 + 7 取余数后的值。

【解题思路】
1. 三个变量，维护中间，初始的时候右框全满，拿出一个，左框空着去比，然后塞入左框
2. 取余，质数
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 1_000_000_007
        suf = Counter(nums)
        ans = 0
        pre = defaultdict(int)
        for idx, x in enumerate(nums):
            suf[x] -= 1
            ans += pre[x * 2] * suf[x * 2]
            pre[x] += 1
        return ans % MOD


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.specialTriplets(nums=[6, 3, 6]))
    print(solution.specialTriplets(nums=[0, 1, 0, 0]))
    print(solution.specialTriplets(nums=[8, 4, 2, 8, 4]))
