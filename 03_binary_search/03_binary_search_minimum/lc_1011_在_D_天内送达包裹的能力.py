# 1011. 在 D 天内送达包裹的能力
"""
传送带上的包裹必须在 days 天内从一个港口运送到另一个港口。

传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量（weights）的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

返回能在 days 天内将传送带上的所有包裹送达的船的最低运载能力。



示例 1：

输入：weights = [1,2,3,4,5,6,7,8,9,10], days = 5
输出：15
解释：
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10

请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。

示例 2：

输入：weights = [3,2,2,4,1,4], days = 3
输出：6
解释：
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4

【解题思路】
1. 要求是在days天内运完，所以当每天只1重量的时候，一直到最大，单调的，二分答案
2. 要统计的是天数，运不下的要留着第二天
3. left需要选最重的，才能运到，不然选1，货运不走，right要选总和，一次全运完
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """

        def check(mid: int) -> bool:
            total = 0
            day = 1
            for i in weights:
                total += i
                if total > mid:
                    day += 1
                    total = i
            return day <= days

        left, right = min(weights), sum(weights)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5))
    print(solution.shipWithinDays(weights=[3, 2, 2, 4, 1, 4], days=3))
