# 2300. 咒语和药水的成功对数
"""
给你两个正整数数组 spells 和 potions ，长度分别为 n 和 m ，其中 spells[i] 表示第 i 个咒语的能量强度，potions[j] 表示第 j 瓶药水的能量强度。

同时给你一个整数 success 。一个咒语和药水的能量强度 相乘 如果 大于等于 success ，那么它们视为一对 成功 的组合。

请你返回一个长度为 n 的整数数组 pairs，其中 pairs[i] 是能跟第 i 个咒语成功组合的 药水 数目。
【解题思路】
1. spells的顺序不能变，potions可以变，给potions排序，然后遍历spell，二分potion，目标是success/spells

"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def lower_bound(self, potions: list[int], target: int) -> int:
        left, right = 0, len(potions) - 1
        while left <= right:
            mid = (left + right) // 2
            if potions[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        ans = []
        potions.sort()
        for i in spells:
            point = self.lower_bound(potions, success / i)
            ans.append(len(potions) - point)
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.successfulPairs(spells=[3, 1, 2], potions=[8, 5, 8], success=16))
