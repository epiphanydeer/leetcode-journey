# 1176. 健身计划评估
'''
一个节食者在第 i 天消耗 calories[i] 卡路里。

给定一个整数 k，对于每个连续的 k 天序列（对于所有的 0 <= i <= n-k，有 calories[i], calories[i+1], ..., calories[i+k-1]），他们想要知道 T，即在这 k 天序列期间消耗的总卡路里（calories[i] + calories[i+1] + ... + calories[i+k-1]）：

如果 T < lower，那么这份计划相对糟糕，并失去 1 分；
如果 T > upper，那么这份计划相对优秀，并获得 1 分；
否则，这份计划普普通通，分值不做变动。

请返回统计完所有 calories.length 天后得到的总分作为评估结果。

注意：总分可能是负数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
