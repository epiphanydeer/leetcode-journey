# 2433. 找出前缀异或的原始数组
'''
给你一个长度为 n 的 整数 数组 pref 。找出并返回满足下述条件且长度为 n 的数组 arr ：

 pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].

注意 ^ 表示 按位异或（bitwise-xor）运算。

可以证明答案是 唯一 的。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
