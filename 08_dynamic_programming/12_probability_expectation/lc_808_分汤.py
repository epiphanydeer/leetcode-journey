# 808. 分汤
'''
你有两种汤，A 和 B，每种初始为 n 毫升。在每一轮中，会随机选择以下四种操作中的一种，每种操作的概率为 0.25，且与之前的所有轮次 无关：

 从汤 A 取 100 毫升，从汤 B 取 0 毫升

 从汤 A 取 75 毫升，从汤 B 取 25 毫升

 从汤 A 取 50 毫升，从汤 B 取 50 毫升

 从汤 A 取 25 毫升，从汤 B 取 75 毫升

注意：

 不存在从汤 A 取 0 ml 和从汤 B 取 100 ml 的操作。

 汤 A 和 B 在每次操作中同时被取出。

 如果一次操作要求你取出比剩余的汤更多的量，请取出该汤剩余的所有部分。

操作过程在任何回合中任一汤被取完后立即停止。

返回汤 A 在 B 前取完的概率，加上两种汤在 同一回合 取完概率的一半。返回值在正确答案 10-5 的范围内将被认为是正确的。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
