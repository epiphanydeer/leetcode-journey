# 2381. 字母移位 II
'''
给你一个小写英文字母组成的字符串 s 和一个二维整数数组 shifts ，其中 shifts[i] = [starti, endi, directioni] 。对于每个 i ，将 s 中从下标 starti 到下标 endi （两者都包含）所有字符都进行移位运算，如果 directioni = 1 将字符向后移位，如果 directioni = 0 将字符向前移位。

将一个字符 向后 移位的意思是将这个字符用字母表中 下一个 字母替换（字母表视为环绕的，所以 'z' 变成 'a'）。类似的，将一个字符 向前 移位的意思是将这个字符用字母表中 前一个 字母替换（字母表是环绕的，所以 'a' 变成 'z' ）。

请你返回对 s 进行所有移位操作以后得到的最终字符串。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
