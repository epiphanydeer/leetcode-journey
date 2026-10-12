# 1209. 删除字符串中的所有相邻重复项 II
'''
给你一个字符串 s，「k 倍重复项删除操作」将会从 s 中选择 k 个相邻且相等的字母，并删除它们，使被删去的字符串的左侧和右侧连在一起。

你需要对 s 重复进行无限次这样的删除操作，直到无法继续为止。

在执行完所有删除操作后，返回最终得到的字符串。

本题答案保证唯一。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
