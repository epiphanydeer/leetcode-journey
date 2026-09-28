# 2132. 用邮票贴满网格图
'''
给你一个 m x n 的二进制矩阵 grid ，每个格子要么为 0 （空）要么为 1 （被占据）。

给你邮票的尺寸为 stampHeight x stampWidth 。我们想将邮票贴进二进制矩阵中，且满足以下 限制 和 要求 ：

 覆盖所有 空 格子。

 不覆盖任何 被占据 的格子。

 我们可以放入任意数目的邮票。

 邮票可以相互有 重叠 部分。

 邮票不允许 旋转 。

 邮票必须完全在矩阵 内 。

如果在满足上述要求的前提下，可以放入邮票，请返回 true ，否则返回 false 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def possibleToStamp(self, grid, stampHeight, stampWidth):
        """
        :type grid: List[List[int]]
        :type stampHeight: int
        :type stampWidth: int
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
