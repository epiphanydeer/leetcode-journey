# 面试题 16.06. 最小差
"""
给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差
【解题思路】
1. 排序，然后要他俩差最小，也就是俩数去互相比较，谁小谁往前走
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def smallestDifference(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: int
        """
        a.sort()
        b.sort()
        left, right = 0, 0
        ans = inf
        while left < len(a) and right < len(b):
            ans = min(ans, abs(a[left] - b[right]))
            if a[left] > b[right]:
                right += 1
            else:
                left += 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestDifference([0], [2147483647]))
