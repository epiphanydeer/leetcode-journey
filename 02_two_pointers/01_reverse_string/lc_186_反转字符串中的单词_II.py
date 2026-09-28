# 186. 反转字符串中的单词 II
'''
给你一个字符数组 s，反转其中单词的顺序。

单词的定义为：单词是一个由非空格字符组成的序列。s 中的单词将会由单个空格分隔。

必须设计并实现原地解法来解决此问题，即不分配额外的空间。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
