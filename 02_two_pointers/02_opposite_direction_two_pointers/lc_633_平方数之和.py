# 633. 平方数之和
"""
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
【解题思路】
1. 最初设想是俩指针从1到num-1开始算，后来看可以从1到sqrt(num)，这样更方便
2. 注意这里可以left = right，因为特殊条件2 = 1*1 + 1*1
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left, right = 0, isqrt(c)
        while left <= right:
            s = left * left + right * right
            if s == c:
                return True
            elif s > c:
                right -= 1
            else:
                left += 1
        return False


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.judgeSquareSum(c=5))
