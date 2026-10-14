# 2747. 统计没有收到请求的服务器数目
'''
给你一个整数 n ，表示服务器的总数目，再给你一个下标从 0 开始的 二维 整数数组 logs ，其中 logs[i] = [server_id, time] 表示 id 为 server_id 的服务器在 time 时收到了一个请求。

同时给你一个整数 x 和一个下标从 0 开始的整数数组 queries  。

请你返回一个长度等于 queries.length 的数组 arr ，其中 arr[i] 表示在时间区间 [queries[i] - x, queries[i]] 内没有收到请求的服务器数目。

注意时间区间是个闭区间。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countServers(self, n, logs, x, queries):
        """
        :type n: int
        :type logs: List[List[int]]
        :type x: int
        :type queries: List[int]
        :rtype: List[int]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
