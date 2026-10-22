# 1385. 两个数组间的距离值
"""
给你两个整数数组 arr1 ， arr2 和一个整数 d ，请你返回两个数组之间的 距离值 。

「距离值」 定义为符合此距离要求的元素数目：对于元素 arr1[i] ，不存在任何元素 arr2[j] 满足 |arr1[i]-arr2[j]| <= d 。
【解题思路】
1. 先排序，然后就对着arr1的数字，算出左边界和右边界，只要arr2在边界内没有数字，就可以
2. 边界怎么写：arr1的数-2是左边界，然后看刚好小于边界的下一个数是否在右边界外面就可以了
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr1.sort()
        arr2.sort()
        right = 0
        ans = 0
        for i in arr1:
            while right < len(arr2) and arr2[right] < i - d:
                right += 1
            if right == len(arr2) or arr2[right] > i + d:
                ans += 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(
        solution.findTheDistanceValue(
            arr1=[2, 1, 100, 3], arr2=[-5, -2, 10, -3, 7], d=6
        )
    )
