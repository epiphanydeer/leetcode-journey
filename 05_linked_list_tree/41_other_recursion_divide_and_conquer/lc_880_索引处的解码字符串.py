# 880. 索引处的解码字符串
'''
给定一个编码字符串 s 。请你找出 解码字符串 并将其写入磁带。解码时，从编码字符串中 每次读取一个字符 ，并采取以下步骤：

 如果所读的字符是字母，则将该字母写在磁带上。

 如果所读的字符是数字（例如 d），则整个当前磁带总共会被重复写 d-1 次。

现在，对于给定的编码字符串 s 和索引 k，查找并返回解码字符串中的第 k 个字母。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def decodeAtIndex(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
