# 2486. 追加字符以获得子序列
'''
给你两个仅由小写英文字母组成的字符串 s 和 t 。

现在需要通过向 s 末尾追加字符的方式使 t 变成 s 的一个 子序列 ，返回需要追加的最少字符数。

子序列是一个可以由其他字符串删除部分（或不删除）字符但不改变剩下字符顺序得到的字符串。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
