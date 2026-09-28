# 2606. 找到最大开销的子字符串
'''
给你一个字符串 s ，一个字符 互不相同 的字符串 chars 和一个长度与 chars 相同的整数数组 vals 。

子字符串的开销 是一个子字符串中所有字符对应价值之和。空字符串的开销是 0 。

字符的价值 定义如下：

 如果字符不在字符串 chars 中，那么它的价值是它在字母表中的位置（下标从 1 开始）。

 
 比方说，'a' 的价值为 1 ，'b' 的价值为 2 ，以此类推，'z' 的价值为 26 。

 
 

 否则，如果这个字符在 chars 中的位置为 i ，那么它的价值就是 vals[i] 。

请你返回字符串 s 的所有子字符串中的最大开销。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maximumCostSubstring(self, s, chars, vals):
        """
        :type s: str
        :type chars: str
        :type vals: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
