# 1930. 长度为 3 的不同回文子序列
'''
给你一个字符串 s ，返回 s 中 长度为 3 的不同回文子序列 的个数。

即便存在多种方法来构建相同的子序列，但相同的子序列只计数一次。

回文 是正着读和反着读一样的字符串。

子序列 是由原字符串删除其中部分字符（也可以不删除）且不改变剩余字符之间相对顺序形成的一个新字符串。

 例如，"ace" 是 "abcde" 的一个子序列。
'''

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

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
