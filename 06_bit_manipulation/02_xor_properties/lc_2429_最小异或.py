# 2429. 最小异或
'''
给你两个正整数 num1 和 num2 ，找出满足下述条件的正整数 x ：

 x 的置位数和 num2 相同，且

 x XOR num1 的值 最小

注意 XOR 是按位异或运算。

返回整数 x 。题目保证，对于生成的测试用例， x 是 唯一确定 的。

整数的 置位数 是其二进制表示中 1 的数目。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
