# 3. 无重复字符的最长子串
"""
给定一个字符串s，请你找出其中不含有重复字符的最长子串的长度。
【解题思路】
1. 看到不重复，考虑使用defaultdict
2. 看到最长子串，考虑滑窗，发现是不定长，并且最长，则while条件不对就开始缩
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, left = 0, 0
        d = defaultdict(int)
        for right, j in enumerate(s):
            d[j] += 1
            while d[j] > 1:
                d[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s="abcabcbb"))
