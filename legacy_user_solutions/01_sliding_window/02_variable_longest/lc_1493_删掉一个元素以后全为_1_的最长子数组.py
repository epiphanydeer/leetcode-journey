# 1493. 删掉一个元素以后全为 1 的最长子数组
"""
给你一个二进制数组 nums ，你需要从中删掉一个元素。
请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。
如果不存在这样的子数组，请返回 0 。
提示 1：

输入：nums = [1,1,0,1]
输出：3
解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。
【解题思路】
1. 也就是要找最长1的子数组，里面只能有1个0
2. 最长，子数组： 不定滑块
3. 因为都是0，1 就不用字典了，我的想法是设置个0的flag，大于1了就开始缩
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, flag, left = 0, 0, 0
        for right, j in enumerate(nums):
            if j == 0:
                flag += 1
            while flag > 1:
                flag -= 1 - nums[left]
                left += 1
            ans = max(ans, right - left)
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
