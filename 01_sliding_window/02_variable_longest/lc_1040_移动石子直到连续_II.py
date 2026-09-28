# 1040. 移动石子直到连续 II
'''
在 X 轴上有一些不同位置的石子。给定一个整数数组 stones 表示石子的位置。

如果一个石子在最小或最大的位置，称其为 端点石子。每个回合，你可以将一颗 端点石子 拿起并移动到一个未占用的位置，使得该石子不再是一颗 端点石子。

 值得注意的是，如果石子像 stones = [1,2,5] 这样，你将 无法 移动位于位置 5 的端点石子，因为无论将它移动到任何位置（例如 0 或 3），该石子都仍然会是端点石子。

当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。

以长度为 2 的数组形式返回答案，其中：

 answer[0] 是你可以移动的最小次数

 answer[1] 是你可以移动的最大次数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def numMovesStonesII(self, stones):
        """
        :type stones: List[int]
        :rtype: List[int]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
