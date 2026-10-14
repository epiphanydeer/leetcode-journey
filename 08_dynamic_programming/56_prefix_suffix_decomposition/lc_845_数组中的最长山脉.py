# 845. 数组中的最长山脉
'''
把符合下列属性的数组 arr 称为 山脉数组 ：

 arr.length >= 3

 存在下标 i（0 < i < arr.length - 1），满足
 
 arr[0] < arr[1] < ... < arr[i - 1] < arr[i]

 arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 
 

给出一个整数数组 arr，返回最长山脉子数组的长度。如果不存在山脉子数组，返回 0 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
