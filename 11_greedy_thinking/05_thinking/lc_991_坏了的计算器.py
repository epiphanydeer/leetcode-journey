# 991. 坏了的计算器
'''
在显示着数字 startValue 的坏计算器上，我们可以执行以下两种操作：

 双倍（Double）：将显示屏上的数字乘 2；

 递减（Decrement）：将显示屏上的数字减 1 。

给定两个整数 startValue 和 target 。返回显示数字 target 所需的最小操作数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
