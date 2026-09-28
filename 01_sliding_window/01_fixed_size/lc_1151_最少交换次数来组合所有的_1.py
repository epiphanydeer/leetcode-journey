# 1151. 最少交换次数来组合所有的 1
'''
给出一个二进制数组 data，你需要通过交换位置，将数组中任何位置上的 1 组合到一起，并返回所有可能中所需最少的交换次数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minSwaps(self, data):
        """
        :type data: List[int]
        :rtype: int
        """
        

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
