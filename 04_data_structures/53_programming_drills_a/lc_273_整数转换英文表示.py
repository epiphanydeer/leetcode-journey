# 273. 整数转换英文表示
'''
将非负整数 num 转换为其对应的英文表示。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
