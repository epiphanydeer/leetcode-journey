# 2484. 统计回文子序列数目
'''
给你数字字符串 s ，请你返回 s 中长度为 5 的 回文子序列 数目。由于答案可能很大，请你将答案对 109 + 7 取余 后返回。

提示：

 如果一个字符串从前往后和从后往前读相同，那么它是 回文字符串 。

 子序列是一个字符串中删除若干个字符后，不改变字符顺序，剩余字符构成的字符串。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countPalindromes(self, s):
        """
        :type s: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
