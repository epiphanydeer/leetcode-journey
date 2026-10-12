# 1307. 口算难题
'''
给你一个方程，左边用 words 表示，右边用 result 表示。

你需要根据以下规则检查方程是否可解：

 每个字符都会被解码成一位数字（0 - 9）。

 每对不同的字符必须映射到不同的数字。

 每个 words[i] 和 result 都会被解码成一个没有前导零的数字。

 左侧数字之和（words）等于右侧数字（result）。 

如果方程可解，返回 True，否则返回 False。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def isSolvable(self, words, result):
        """
        :type words: List[str]
        :type result: str
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
