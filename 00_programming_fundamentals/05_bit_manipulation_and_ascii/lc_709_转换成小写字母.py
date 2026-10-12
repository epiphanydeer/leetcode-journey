# 709. 转换成小写字母
'''
给你一个字符串 s ，将该字符串中的大写字母转换成相同的小写字母，返回新的字符串。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
