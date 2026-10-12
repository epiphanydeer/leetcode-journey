# 1079. 活字印刷
'''
你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。

注意：本题中，每个活字字模只能使用一次。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
