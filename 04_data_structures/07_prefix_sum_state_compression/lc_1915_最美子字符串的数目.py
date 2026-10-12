# 1915. 最美子字符串的数目
'''
如果某个字符串中 至多一个 字母出现 奇数 次，则称其为 最美 字符串。

 例如，"ccjjc" 和 "abab" 都是最美字符串，但 "ab" 不是。

给你一个字符串 word ，该字符串由前十个小写英文字母组成（'a' 到 'j'）。请你返回 word 中 最美非空子字符串 的数目。如果同样的子字符串在 word 中出现多次，那么应当对 每次出现 分别计数。

子字符串 是字符串中的一个连续字符序列。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
