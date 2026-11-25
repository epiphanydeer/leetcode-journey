# 1930. 长度为 3 的不同回文子序列
"""
给你一个字符串 s ，返回 s 中 长度为 3 的不同回文子序列 的个数。

即便存在多种方法来构建相同的子序列，但相同的子序列只计数一次。

回文 是正着读和反着读一样的字符串。

子序列 是由原字符串删除其中部分字符（也可以不删除）且不改变剩余字符之间相对顺序形成的一个新字符串。

 例如，"ace" 是 "abcde" 的一个子序列。
 【解题思路】
 1. 遍历中间的，两边的字符相等就可以了
 2. 因为要不同子序列，所以用set，然后add
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        suf = Counter(s)
        pre = defaultdict(int)
        ans = set()
        for idx, x in enumerate(s):
            suf[x] -= 1
            for i in pre:
                if pre[i] > 0 and suf[i] > 0:
                    ans.add((x, i))
            pre[x] += 1
        return len(ans)


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.countPalindromicSubsequence(s="aabca"))
    print(solution.countPalindromicSubsequence(s="adc"))
    print(solution.countPalindromicSubsequence(s="bbcbaba"))
