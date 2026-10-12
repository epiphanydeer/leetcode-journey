# 933. 最近的请求次数
'''
写一个 RecentCounter 类来计算特定时间范围内最近的请求。

请你实现 RecentCounter 类：

 RecentCounter() 初始化计数器，请求数为 0 。

 int ping(int t) 在时间 t 添加一个新请求，其中 t 表示以毫秒为单位的某个时间，然后返回在包含范围 [t - 3000, t] 内发生的请求数量，即新请求加上所有早于或等于 3000 毫秒前的请求。

保证 每次对 ping 的调用都使用比之前更大的 t 值。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class RecentCounter(object):

    def __init__(self):
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
