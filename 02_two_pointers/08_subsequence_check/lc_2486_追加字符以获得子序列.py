# 2486. 追加字符以获得子序列
"""
给你两个仅由小写英文字母组成的字符串 s 和 t 。

现在需要通过向 s 末尾追加字符的方式使 t 变成 s 的一个 子序列 ，返回需要追加的最少字符数。

子序列是一个可以由其他字符串删除部分（或不删除）字符但不改变剩下字符顺序得到的字符串。
【解题思路】
1. 让t变成s的子序列，那就遍历s，看s里有多少含t的东西
2. 双指针
"""

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
        j = 0
        for i in s:
            if j < len(t) and t[j] == i:
                j += 1
        return len(t) - j


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.appendCharacters(s="coaching", t="coding"))
