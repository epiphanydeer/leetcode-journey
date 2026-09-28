# 2833. 距离原点最远的点
'''
给你一个长度为 n 的字符串 moves ，该字符串仅由字符 'L'、'R' 和 '_' 组成。字符串表示你在一条原点为 0 的数轴上的若干次移动。

你的初始位置就在原点（0），第 i 次移动过程中，你可以根据对应字符选择移动方向：

 如果 moves[i] = 'L' 或 moves[i] = '_' ，可以选择向左移动一个单位距离

 如果 moves[i] = 'R' 或 moves[i] = '_' ，可以选择向右移动一个单位距离

返回在移动 n 次之后，可以到达的距离原点 最远 的点 到原点的距离。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
