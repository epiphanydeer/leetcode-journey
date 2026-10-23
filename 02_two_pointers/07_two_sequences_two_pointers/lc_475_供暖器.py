# 475. 供暖器
"""
冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
在加热器的加热半径范围内的每个房屋都可以获得供暖。
现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。
注意：所有供暖器 heaters 都遵循你的半径标准，加热的半径也一样。
【解题思路】
1. 也就是遍历一下房屋，找最近的供暖器，然后对所有的房屋的距离找最大值
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        j = 0
        ans = 0
        for i in houses:
            distance = abs(i - heaters[j])
            while j + 1 < len(heaters) and distance >= abs(i - heaters[j + 1]):
                distance = abs(i - heaters[j + 1])
                j += 1
            ans = max(ans, distance)
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.findRadius(houses=[1, 2, 3, 4], heaters=[1, 4]))
