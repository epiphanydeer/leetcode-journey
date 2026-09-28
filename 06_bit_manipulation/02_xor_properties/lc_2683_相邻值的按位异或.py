# 2683. 相邻值的按位异或
'''
下标从 0 开始、长度为 n 的数组 derived 是由同样长度为 n 的原始 二进制数组 original 通过计算相邻值的 按位异或（⊕）派生而来。

特别地，对于范围 [0, n - 1] 内的每个下标 i ：

 如果 i = n - 1 ，那么 derived[i] = original[i] ⊕ original[0]

 否则 derived[i] = original[i] ⊕ original[i + 1]

给你一个数组 derived ，请判断是否存在一个能够派生得到 derived 的 有效原始二进制数组 original 。

如果存在满足要求的原始二进制数组，返回 true ；否则，返回 false 。

 二进制数组是仅由 0 和 1 组成的数组。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
