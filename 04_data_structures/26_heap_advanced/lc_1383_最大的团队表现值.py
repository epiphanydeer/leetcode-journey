# 1383. 最大的团队表现值
'''
给定两个整数 n 和 k，以及两个长度为 n 的整数数组 speed 和 efficiency。现有 n 名工程师，编号从 1 到 n。其中 speed[i] 和 efficiency[i] 分别代表第 i 位工程师的速度和效率。

从这 n 名工程师中最多选择 k 名不同的工程师，使其组成的团队具有最大的团队表现值。

团队表现值 的定义为：一个团队中「所有工程师速度的和」乘以他们「效率值中的最小值」。

请你返回该团队的​​​​​​最大团队表现值，由于答案可能很大，请你返回结果对 10^9 + 7 取余后的结果。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
