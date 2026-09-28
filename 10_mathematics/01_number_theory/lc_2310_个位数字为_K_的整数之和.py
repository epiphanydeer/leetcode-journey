# 2310. 个位数字为 K 的整数之和
'''
给你两个整数 num 和 k ，考虑具有以下属性的正整数多重集：

 每个整数个位数字都是 k 。

 所有整数之和是 num 。

返回该多重集的最小大小，如果不存在这样的多重集，返回 -1 。

注意：

 多重集与集合类似，但多重集可以包含多个同一整数，空多重集的和为 0 。

 个位数字 是数字最右边的数位。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minimumNumbers(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
