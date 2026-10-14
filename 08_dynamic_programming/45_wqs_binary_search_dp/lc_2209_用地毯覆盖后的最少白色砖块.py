# 2209. 用地毯覆盖后的最少白色砖块
'''
给你一个下标从 0 开始的 二进制 字符串 floor ，它表示地板上砖块的颜色。

 floor[i] = '0' 表示地板上第 i 块砖块的颜色是 黑色 。

 floor[i] = '1' 表示地板上第 i 块砖块的颜色是 白色 。

同时给你 numCarpets 和 carpetLen 。你有 numCarpets 条 黑色 的地毯，每一条 黑色 的地毯长度都为 carpetLen 块砖块。请你使用这些地毯去覆盖砖块，使得未被覆盖的剩余 白色 砖块的数目 最小 。地毯相互之间可以覆盖。

请你返回没被覆盖的白色砖块的 最少 数目。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minimumWhiteTiles(self, floor, numCarpets, carpetLen):
        """
        :type floor: str
        :type numCarpets: int
        :type carpetLen: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
