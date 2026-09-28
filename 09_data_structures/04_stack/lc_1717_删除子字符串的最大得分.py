# 1717. 删除子字符串的最大得分
'''
给你一个字符串 s 和两个整数 x 和 y 。你可以执行下面两种操作任意次。

 删除子字符串 "ab" 并得到 x 分。

 
 比方说，从 "cabxbae" 删除 ab ，得到 "cxbae" 。

 
 

 删除子字符串"ba" 并得到 y 分。
 
 比方说，从 "cabxbae" 删除 ba ，得到 "cabxe" 。

 
 

请返回对 s 字符串执行上面操作若干次能得到的最大得分。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
