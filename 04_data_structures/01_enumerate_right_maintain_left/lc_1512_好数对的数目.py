# 1512. 好数对的数目
"""
给你一个整数数组 nums 。

如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。

返回好数对的数目。
【解题思路】
1. 只要数字相等并且序号小的就可以加1
2. 所以用哈希表计数，然后遍历数组先求和，再计数
3. 这里用的是求数组个数，求增量，+=left
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(int)
        ans = 0
        for x in nums:
            ans += d[x]
            d[x] += 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]))
    print(solution.numIdenticalPairs(nums=[1, 1, 1, 1]))
