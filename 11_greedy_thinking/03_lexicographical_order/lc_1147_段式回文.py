# 1147. 段式回文
'''
你会得到一个字符串 text 。你应该把它分成 k 个子字符串 (subtext1, subtext2，…， subtextk) ，要求满足:

 subtexti 是 非空 字符串

 所有子字符串的连接等于 text ( 即subtext1 + subtext2 + ... + subtextk == text )

 对于所有 i 的有效值( 即 1 <= i <= k ) ，subtexti == subtextk - i + 1 均成立

返回k可能最大值。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def longestDecomposition(self, text):
        """
        :type text: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
