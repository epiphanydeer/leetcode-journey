# 904. 水果成篮
"""
你正在探访一家农场，农场从左到右种植了一排果树。这些树用一个整数数组 fruits 表示，其中 fruits[i] 是第 i 棵树上的水果 种类 。
你想要尽可能多地收集水果。然而，农场的主人设定了一些严格的规矩，你必须按照要求采摘水果：
 你只有 两个 篮子，并且每个篮子只能装 单一类型 的水果。每个篮子能够装的水果总量没有限制。
 你可以选择任意一棵树开始采摘，你必须从 每棵 树（包括开始采摘的树）上 恰好摘一个水果 。采摘的水果应当符合篮子中的水果类型。每采摘一次，你将会向右移动到下一棵树，并继续采摘。
 一旦你走到某棵树前，但水果不符合篮子的水果类型，那么就必须停止采摘。
给你一个整数数组 fruits ，返回你可以收集的水果的 最大 数目。
【解题思路】
1. 就是两个篮子，分别只能装相同数字的水果，并且中途不能停，因此为滑窗
2. 人话就是最多两种元素的最大长度，返回长度
3. 元素要计数，哈希表+滑窗
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        d = defaultdict(int)
        ans, left = 0, 0
        for right, j in enumerate(fruits):
            d[j] += 1
            while len(d) > 2:
                d[fruits[left]] -= 1
                if d[fruits[left]] == 0:
                    del d[fruits[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.totalFruit(fruits=[1, 2, 3, 2, 2]))
