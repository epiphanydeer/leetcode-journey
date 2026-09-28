# 1657. 确定两个字符串是否接近
'''
如果可以使用以下操作从一个字符串得到另一个字符串，则认为两个字符串 接近 ：

 操作 1：交换任意两个 现有 字符。

 
 例如，abcde -> aecdb

 
 

 操作 2：将一个 现有 字符的每次出现转换为另一个 现有 字符，并对另一个字符执行相同的操作。
 
 例如，aacabb -> bbcbaa（所有 a 转化为 b ，而所有的 b 转换为 a ）

 
 

你可以根据需要对任意一个字符串多次使用这两种操作。

给你两个字符串，word1 和 word2 。如果 word1 和 word2 接近 ，就返回 true ；否则，返回 false 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
