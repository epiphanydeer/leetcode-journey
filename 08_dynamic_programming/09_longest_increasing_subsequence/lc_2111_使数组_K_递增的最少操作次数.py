# 2111. 使数组 K 递增的最少操作次数
'''
给你一个下标从 0 开始包含 n 个正整数的数组 arr ，和一个正整数 k 。

如果对于每个满足 k <= i <= n-1 的下标 i ，都有 arr[i-k] <= arr[i] ，那么我们称 arr 是 K 递增 的。

 比方说，arr = [4, 1, 5, 2, 6, 2] 对于 k = 2 是 K 递增的，因为：

 
 arr[0] <= arr[2] (4 <= 5)

 arr[1] <= arr[3] (1 <= 2)

 arr[2] <= arr[4] (5 <= 6)

 arr[3] <= arr[5] (2 <= 2)

 
 

 但是，相同的数组 arr 对于 k = 1 不是 K 递增的（因为 arr[0] > arr[1]），对于 k = 3 也不是 K 递增的（因为 arr[0] > arr[3] ）。

每一次 操作 中，你可以选择一个下标 i 并将 arr[i] 改成任意 正整数。

请你返回对于给定的 k ，使数组变成 K 递增的 最少操作次数 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def kIncreasing(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
