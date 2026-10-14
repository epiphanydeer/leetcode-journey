# 1420. 生成数组
'''
给定三个整数 n、m 和 k 。考虑使用下图描述的算法找出正整数数组中最大的元素。

请你构建一个具有以下属性的数组 arr ：

 arr 中包含确切的 n 个整数。

 1 <= arr[i] <= m 其中 (0 <= i < n) 。

 将上面提到的算法应用于 arr 之后，search_cost 的值等于 k 。

返回在满足上述条件的情况下构建数组 arr 的 方法数量 ，由于答案可能会很大，所以 必须 对 10^9 + 7 取余。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def numOfArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
