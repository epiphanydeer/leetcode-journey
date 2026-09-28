# 37. 解数独
'''
编写一个程序，通过填充空格来解决数独问题。

数独的解法需 遵循如下规则：

 数字 1-9 在每一行只能出现一次。

 数字 1-9 在每一列只能出现一次。

 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）

数独部分空格内已填入了数字，空白格用 '.' 表示。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
