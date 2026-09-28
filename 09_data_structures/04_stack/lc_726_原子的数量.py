# 726. 原子的数量
'''
给你一个字符串化学式 formula ，返回 每种原子的数量 。

原子总是以一个大写字母开始，接着跟随 0 个或任意个小写字母，表示原子的名字。

如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。

 例如，"H2O" 和 "H2O2" 是可行的，但 "H1O2" 这个表达是不可行的。

两个化学式连在一起可以构成新的化学式。

 例如 "H2O2He3Mg4" 也是化学式。

由括号括起的化学式并佐以数字（可选择性添加）也是化学式。

 例如 "(H2O2)" 和 "(H2O2)3" 是化学式。

返回所有原子的数量，格式为：第一个（按字典序）原子的名字，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
