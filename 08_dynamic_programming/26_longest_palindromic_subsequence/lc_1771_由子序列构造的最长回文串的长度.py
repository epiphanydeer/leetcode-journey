# 1771. 由子序列构造的最长回文串的长度
'''
给你两个字符串 word1 和 word2 ，请你按下述方法构造一个字符串：

 从 word1 中选出某个 非空 子序列 subsequence1 。

 从 word2 中选出某个 非空 子序列 subsequence2 。

 连接两个子序列 subsequence1 + subsequence2 ，得到字符串。

返回可按上述方法构造的最长 回文串 的 长度 。如果无法构造回文串，返回 0 。

字符串 s 的一个 子序列 是通过从 s 中删除一些（也可能不删除）字符而不更改其余字符的顺序生成的字符串。

回文串 是正着读和反着读结果一致的字符串。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def longestPalindrome(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
