# 856. 括号的分数
'''
给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：

 () 得 1 分。

 AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。

 (A) 得 2 * A 分，其中 A 是平衡括号字符串。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
