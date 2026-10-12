# 282. 给表达式添加运算符
'''
给定一个仅包含数字 0-9 的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、- 或 * ，返回 所有 能够得到 target 的表达式。

注意，返回表达式中的操作数 不应该 包含前导零。

注意，一个数字可以包含多个数位。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
