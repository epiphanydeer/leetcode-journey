# 2698. 求一个整数的惩罚数
'''
给你一个正整数 n ，请你返回 n 的 惩罚数 。

n 的 惩罚数 定义为所有满足以下条件 i 的数的平方和：

 1 <= i <= n

 i * i 的十进制表示的字符串可以分割成若干连续子字符串，且这些子字符串对应的整数值之和等于 i 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
