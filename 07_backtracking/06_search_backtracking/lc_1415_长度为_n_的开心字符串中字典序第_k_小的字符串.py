# 1415. 长度为 n 的开心字符串中字典序第 k 小的字符串
'''
一个 「开心字符串」定义为：

 仅包含小写字母 ['a', 'b', 'c'].

 对所有在 1 到 s.length - 1 之间的 i ，满足 s[i] != s[i + 1] （字符串的下标从 1 开始）。

比方说，字符串 "abc"，"ac"，"b" 和 "abcbabcbcb" 都是开心字符串，但是 "aa"，"baa" 和 "ababbc" 都不是开心字符串。

给你两个整数 n 和 k ，你需要将长度为 n 的所有开心字符串按字典序排序。

请你返回排序后的第 k 个开心字符串，如果长度为 n 的开心字符串少于 k 个，那么请你返回 空字符串 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
