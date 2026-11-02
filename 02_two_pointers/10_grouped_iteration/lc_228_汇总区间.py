# 228. 汇总区间
"""
给定一个  无重复元素 的 有序 整数数组 nums 。

区间 [a,b] 是从 a 到 b（包含）的所有整数的集合。

返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个区间但不属于 nums 的数字 x 。
列表中的每个区间范围 [a,b] 应该按如下格式输出：
 "a->b" ，如果 a != b
 "a" ，如果 a == b
示例 1：
输入：nums = [0,1,2,4,5,7]
输出：["0->2","4->5","7"]
解释：区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
示例 2：
输入：nums = [0,2,3,4,6,8,9]
输出：["0","2->4","6","8->9"]
解释：区间范围是：
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
【解题思路】
1. 就是找连续的序列，所以只需要判断下一个数是不是-1还等于它
2. 按照题目要求，数组会被分割成若干组，每一组的判断/处理逻辑是相同的。
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i = 0
        n = len(nums)
        ans = []
        while i < n:
            start = i
            i += 1
            while i < n and nums[i] - 1 == nums[i - 1]:
                i += 1
            if i - start == 1:
                ans.append(str(nums[start]))
            else:
                ans.append(f"{nums[start]}->{nums[i-1]}")
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]))
