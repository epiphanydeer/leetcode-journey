# 2063. 所有子字符串中的元音
'''
给你一个字符串 word ，返回 word 的所有子字符串中 元音的总数 ，元音是指 'a'、'e'、'i'、'o' 和 'u' 。

子字符串 是字符串中一个连续（非空）的字符序列。

注意：由于对 word 长度的限制比较宽松，答案可能超过有符号 32 位整数的范围。计算时需当心。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
