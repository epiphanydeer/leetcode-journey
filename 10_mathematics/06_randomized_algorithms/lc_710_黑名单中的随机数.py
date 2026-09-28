# 710. 黑名单中的随机数
'''
给定一个整数 n 和一个 无重复 黑名单整数数组 blacklist 。设计一种算法，从 [0, n - 1] 范围内的任意整数中选取一个 未加入 黑名单 blacklist 的整数。任何在上述范围内且不在黑名单 blacklist 中的整数都应该有 同等的可能性 被返回。

优化你的算法，使它最小化调用语言 内置 随机函数的次数。

实现 Solution 类:

 Solution(int n, int[] blacklist) 初始化整数 n 和被加入黑名单 blacklist 的整数

 int pick() 返回一个范围为 [0, n - 1] 且不在黑名单 blacklist 中的随机整数
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):

    def __init__(self, n, blacklist):
        """
        :type n: int
        :type blacklist: List[int]
        """
        

    def pick(self):
        """
        :rtype: int
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
