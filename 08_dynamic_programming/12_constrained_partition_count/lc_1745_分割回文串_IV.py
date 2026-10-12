# 1745. 分割回文串 IV
'''
给你一个字符串 s ，如果可以将它分割成三个 非空 回文子字符串，那么返回 true ，否则返回 false 。

当一个字符串正着读和反着读是一模一样的，就称其为 回文字符串 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def checkPartitioning(self, s):
        """
        :type s: str
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
