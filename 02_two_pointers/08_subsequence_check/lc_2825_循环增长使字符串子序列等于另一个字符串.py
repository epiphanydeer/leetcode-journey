# 2825. 循环增长使字符串子序列等于另一个字符串
"""
给你一个下标从 0 开始的字符串 str1 和 str2 。
一次操作中，你选择 str1 中的若干下标。对于选中的每一个下标 i ，你将 str1[i] 循环 递增，变成下一个字符。也就是说 'a' 变成 'b' ，'b' 变成 'c' ，以此类推，'z' 变成 'a' 。
如果执行以上操作 至多一次 ，可以让 str2 成为 str1 的子序列，请你返回 true ，否则返回 false 。
注意：一个字符串的子序列指的是从原字符串中删除一些（可以一个字符也不删）字符后，剩下字符按照原本先后顺序组成的新字符串。

【解题思路】
1. ord 加一，额外补充如果是z就判断a
2. 因为只能一次，那就判断+1是否==就可以了
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        if len(s) < len(t):
            return False
        j = 0
        for b in s:
            c = chr(ord(b) + 1) if b != "z" else "a"
            if b == t[j] or c == t[j]:
                j += 1
                if j == len(t):
                    return True
        return False


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.canMakeSubsequence(str1="abc", str2="ad"))
