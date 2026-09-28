# 854. 相似度为 K 的字符串
'''
对于某些非负整数 k ，如果交换 s1 中两个字母的位置恰好 k 次，能够使结果字符串等于 s2 ，则认为字符串 s1 和 s2 的 相似度为 k 。

给你两个字母异位词 s1 和 s2 ，返回 s1 和 s2 的相似度 k 的最小值。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def kSimilarity(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
