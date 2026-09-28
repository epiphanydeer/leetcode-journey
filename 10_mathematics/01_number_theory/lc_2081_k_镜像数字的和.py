# 2081. k 镜像数字的和
'''
一个 k 镜像数字 指的是一个在十进制和 k 进制下从前往后读和从后往前读都一样的 没有前导 0 的 正 整数。

 比方说，9 是一个 2 镜像数字。9 在十进制下为 9 ，二进制下为 1001 ，两者从前往后读和从后往前读都一样。

 相反地，4 不是一个 2 镜像数字。4 在二进制下为 100 ，从前往后和从后往前读不相同。

给你进制 k 和一个数字 n ，请你返回 k 镜像数字中 最小 的 n 个数 之和 。

 

示例 1：

输入：k = 2, n = 5
输出：25
解释：
最小的 5 个 2 镜像数字和它们的二进制表示如下：
 十进制 二进制
 1 1
 3 11
 5 101
 7 111
 9 1001
它们的和为 1 + 3 + 5 + 7 + 9 = 25 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def kMirror(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
