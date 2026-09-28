# 1316. 不同的循环子字符串
'''
给你一个字符串 text ，请你返回满足下述条件的 不同 非空子字符串的数目：

 可以写成某个字符串与其自身相连接的形式（即，可以写为 a + a，其中 a 是某个字符串）。

例如，abcabc 就是 abc 和它自身连接形成的。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def distinctEchoSubstrings(self, text):
        """
        :type text: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
