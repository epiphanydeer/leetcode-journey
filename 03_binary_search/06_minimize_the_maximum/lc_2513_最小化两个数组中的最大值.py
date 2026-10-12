# 2513. 最小化两个数组中的最大值
'''
给你两个数组 arr1 和 arr2 ，它们一开始都是空的。你需要往它们中添加正整数，使它们满足以下条件：

 arr1 包含 uniqueCnt1 个 互不相同 的正整数，每个整数都 不能 被 divisor1 整除 。

 arr2 包含 uniqueCnt2 个 互不相同 的正整数，每个整数都 不能 被 divisor2 整除 。

 arr1 和 arr2 中的元素 互不相同 。

给你 divisor1 ，divisor2 ，uniqueCnt1 和 uniqueCnt2 ，请你返回两个数组中 最大元素 的 最小值 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minimizeSet(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2):
        """
        :type divisor1: int
        :type divisor2: int
        :type uniqueCnt1: int
        :type uniqueCnt2: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
