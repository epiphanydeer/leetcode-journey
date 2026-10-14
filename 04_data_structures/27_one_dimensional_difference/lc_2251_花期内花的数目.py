# 2251. 花期内花的数目
'''
给你一个下标从 0 开始的二维整数数组 flowers ，其中 flowers[i] = [starti, endi] 表示第 i 朵花的 花期 从 starti 到 endi （都 包含）。同时给你一个下标从 0 开始大小为 n 的整数数组 people ，people[i] 是第 i 个人来看花的时间。

请你返回一个大小为 n 的整数数组 answer ，其中 answer[i]是第 i 个人到达时在花期内花的 数目 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        """
        :type flowers: List[List[int]]
        :type people: List[int]
        :rtype: List[int]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
