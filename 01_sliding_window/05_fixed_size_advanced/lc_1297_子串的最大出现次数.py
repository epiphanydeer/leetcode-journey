# 1297. 子串的最大出现次数
'''
给你一个字符串 s ，请你返回满足以下条件且出现次数最大的 任意 子串的出现次数：

 子串中不同字母的数目必须小于等于 maxLetters 。

 子串的长度必须大于等于 minSize 且小于等于 maxSize 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
