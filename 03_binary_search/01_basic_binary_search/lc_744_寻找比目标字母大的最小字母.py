# 744. 寻找比目标字母大的最小字母
"""
给你一个字符数组 letters，该数组按 非递减顺序 排序，以及一个字符 target。letters 里至少有两个不同的字符。

返回 letters 中大于 target 的最小的字符。如果不存在这样的字符，则返回 letters 的第一个字符。
【解题思路】
1. 注意这里找的是比目标字母大的，所以二分应该是大于不是大于等于，修改条件
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def lower_bound(self, letters: list[str], target: str) -> int:
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = self.lower_bound(letters, target)
        if left == len(letters):
            return letters[0]
        else:
            return letters[left]


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.nextGreatestLetter(letters=["c", "f", "j"], target="a"))
