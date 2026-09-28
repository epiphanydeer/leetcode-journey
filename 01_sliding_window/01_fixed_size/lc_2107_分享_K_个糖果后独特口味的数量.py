# 2107. 分享 K 个糖果后独特口味的数量
'''
您将获得一个从 0 开始的整数数组 candies，其中 candies[i] 表示第 i 个糖果的味道。你妈妈想让你和你妹妹分享这些糖果，给她 k 个连续的糖果，但你想保留尽可能多的糖果口味。

在与妹妹分享后，返回最多可保留的独特口味的糖果。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def shareCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
