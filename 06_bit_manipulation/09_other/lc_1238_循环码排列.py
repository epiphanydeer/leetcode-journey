# 1238. 循环码排列
'''
给你两个整数 n 和 start。你的任务是返回任意 (0,1,2,,...,2^n-1) 的排列 p，并且满足：

 p[0] = start

 p[i] 和 p[i+1] 的二进制表示形式只有一位不同

 p[0] 和 p[2^n -1] 的二进制表示形式也只有一位不同
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
