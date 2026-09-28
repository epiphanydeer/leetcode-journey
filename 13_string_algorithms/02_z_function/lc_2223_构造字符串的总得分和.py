# 2223. 构造字符串的总得分和
'''
你需要从空字符串开始 构造 一个长度为 n 的字符串 s ，构造的过程为每次给当前字符串 前面 添加 一个 字符。构造过程中得到的所有字符串编号为 1 到 n ，其中长度为 i 的字符串编号为 si 。

 比方说，s = "abaca" ，s1 == "a" ，s2 == "ca" ，s3 == "aca" 依次类推。

si 的 得分 为 si 和 sn 的 最长公共前缀 的长度（注意 s == sn ）。

给你最终的字符串 s ，请你返回每一个 si 的 得分之和 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def sumScores(self, s):
        """
        :type s: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
