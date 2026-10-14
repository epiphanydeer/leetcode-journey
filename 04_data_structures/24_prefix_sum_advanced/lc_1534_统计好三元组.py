# 1534. 统计好三元组
'''
给你一个整数数组 arr ，以及 a、b 、c 三个整数。请你统计其中好三元组的数量。

如果三元组 (arr[i], arr[j], arr[k]) 满足下列全部条件，则认为它是一个 好三元组 。

 0 <= i < j < k < arr.length

 |arr[i] - arr[j]| <= a

 |arr[j] - arr[k]| <= b

 |arr[i] - arr[k]| <= c

其中 |x| 表示 x 的绝对值。

返回 好三元组的数量 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
