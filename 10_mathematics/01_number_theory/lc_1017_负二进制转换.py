# 1017. 负二进制转换
'''
给你一个整数 n ，以二进制字符串的形式返回该整数的 负二进制（base -2）表示。

注意，除非字符串就是 "0"，否则返回的字符串中不能含有前导零。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def baseNeg2(self, n):
        """
        :type n: int
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
