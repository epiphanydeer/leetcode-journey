# 2156. 查找给定哈希值的子串
'''
给定整数 p 和 m ，一个长度为 k 且下标从 0 开始的字符串 s 的哈希值按照如下函数计算：

 hash(s, p, m) = (val(s[0]) * p0 + val(s[1]) * p1 + ... + val(s[k-1]) * pk-1) mod m.

其中 val(s[i]) 表示 s[i] 在字母表中的下标，从 val('a') = 1 到 val('z') = 26 。

给你一个字符串 s 和整数 power，modulo，k 和 hashValue 。请你返回 s 中 第一个 长度为 k 的 子串 sub ，满足 hash(sub, power, modulo) == hashValue 。

测试数据保证一定 存在 至少一个这样的子串。

子串 定义为一个字符串中连续非空字符组成的序列。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def subStrHash(self, s, power, modulo, k, hashValue):
        """
        :type s: str
        :type power: int
        :type modulo: int
        :type k: int
        :type hashValue: int
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
