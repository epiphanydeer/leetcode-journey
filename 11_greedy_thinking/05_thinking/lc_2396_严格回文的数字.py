# 2396. 严格回文的数字
'''
如果一个整数 n 在 b 进制下（b 为 2 到 n - 2 之间的所有整数）对应的字符串 全部 都是 回文的 ，那么我们称这个数 n 是 严格回文 的。

给你一个整数 n ，如果 n 是 严格回文 的，请返回 true ，否则返回 false 。

如果一个字符串从前往后读和从后往前读完全相同，那么这个字符串是 回文的 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
