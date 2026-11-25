# 1128. 等价多米诺骨牌对的数量
"""
给你一组多米诺骨牌 dominoes 。

形式上，dominoes[i] = [a, b] 与 dominoes[j] = [c, d] 等价 当且仅当 (a == c 且 b == d) 或者 (a == d 且 b == c) 。即一张骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌。

在 0 <= i < j < dominoes.length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量。
【解题思路】
1. 要用哈希表，得是不可变，用tuple，并且顺序无关，用sorted
2. 数量求和越长越合法的方法
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        d = defaultdict(int)
        ans = 0
        for a in dominoes:
            ans += d[tuple(sorted(a))]
            d[tuple(sorted(a))] += 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.numEquivDominoPairs(dominoes=[[1, 2], [2, 1], [3, 4], [5, 6]]))
    print(
        solution.numEquivDominoPairs(dominoes=[[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]])
    )
