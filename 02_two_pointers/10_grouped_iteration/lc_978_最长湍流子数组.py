# 978. 最长湍流子数组
'''
给定一个整数数组 arr ，返回 arr 的 最大湍流子数组的长度 。

如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是 湍流子数组 。

更正式地来说，当 arr 的子数组 A[i], A[i+1], ..., A[j] 满足仅满足下列条件时，我们称其为湍流子数组：

 若 i <= k < j ：

 
 当 k 为奇数时， A[k] > A[k+1]，且

 当 k 为偶数时，A[k] < A[k+1]；

 
 

 或 若 i <= k < j ：
 
 当 k 为偶数时，A[k] > A[k+1] ，且

 当 k 为奇数时， A[k] < A[k+1]。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
