# LCR 180. 文件组合
'''
待传输文件被切分成多个部分，按照原排列顺序，每部分文件编号均为一个 正整数（至少含有两个文件）。传输要求为：连续文件编号总和为接收方指定数字 target 的所有文件。请返回所有符合该要求的文件传输组合列表。

注意，返回时需遵循以下规则：

 每种组合按照文件编号 升序 排列；

 不同组合按照第一个文件编号 升序 排列。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def fileCombination(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
