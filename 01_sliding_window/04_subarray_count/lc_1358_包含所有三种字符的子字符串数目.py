# 1358. 包含所有三种字符的子字符串数目
"""
给你一个字符串 s ，它只包含三种字符 a, b 和 c 。

请你返回 a，b 和 c 都 至少 出现过一次的子字符串数目。
【解题思路】
针对越长越合法的两种解法：
1. 算右边：到刚好符合题意的时候，固定right，right之后的全部都符合条件，也就是+=len(s) - right
2. 算左边：到刚好符合题意的时候，left缩到不合格的地方，意思就是合格的地方的左边加多少都是合格的 += left
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # # 算右边：
        # left, ans = 0, 0
        # n = len(s)
        # d = defaultdict(int)
        # for right, j in enumerate(s):
        #     d[j] += 1
        #     while len(d) >= 3:
        #         ans += n - right
        #         l = s[left]
        #         d[l] -= 1
        #         if d[l] == 0:
        #             del d[l]
        #         left += 1
        # return ans

        # 算右边
        left, ans = 0, 0
        d = defaultdict(int)
        for right, j in enumerate(s):
            d[j] += 1
            while len(d) >= 3:
                d[s[left]] -= 1
                if d[s[left]] == 0:
                    del d[s[left]]
                left += 1
            ans += left
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
