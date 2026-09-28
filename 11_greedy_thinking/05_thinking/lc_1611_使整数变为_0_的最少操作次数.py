# 1611. 使整数变为 0 的最少操作次数
'''
给你一个整数 n，你需要重复执行多次下述操作将其转换为 0 ：

 翻转 n 的二进制表示中最右侧位（第 0 位）。

 如果二进制表示中的第 (i-1) 位为 1 且从第 (i-2) 位到第 0 位都为 0，则翻转 n 的二进制表示中的第 i 位。

返回将 n 转换为 0 的最小操作次数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
