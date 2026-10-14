# 903. DI 序列的有效排列
'''
给定一个长度为 n 的字符串 s ，其中 s[i] 是:

 “D” 意味着减少，或者

 “I” 意味着增加

有效排列 是对有 n + 1 个在 [0, n]  范围内的整数的一个排列 perm ，使得对所有的 i：

 如果 s[i] == 'D'，那么 perm[i] > perm[i+1]，以及；

 如果 s[i] == 'I'，那么 perm[i] < perm[i+1]。

返回 有效排列  perm的数量 。因为答案可能很大，所以请返回你的答案对 109 + 7 取余。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def numPermsDISequence(self, s):
        """
        :type s: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
