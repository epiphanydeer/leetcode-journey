# 984. 不含 AAA 或 BBB 的字符串
'''
给定两个整数 a 和 b ，返回 任意 字符串 s ，要求满足：

 s 的长度为 a + b，且正好包含 a 个 'a' 字母与 b 个 'b' 字母；

 子串 'aaa' 没有出现在 s 中；

 子串 'bbb' 没有出现在 s 中。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def strWithout3a3b(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
