# 650. 两个键的键盘
'''
最初记事本上只有一个字符 'A' 。你每次可以对这个记事本进行两种操作：

 Copy All（复制全部）：复制这个记事本中的所有字符（不允许仅复制部分字符）。

 Paste（粘贴）：粘贴 上一次 复制的字符。

给你一个数字 n ，你需要使用最少的操作次数，在记事本上输出 恰好 n 个 'A' 。返回能够打印出 n 个 'A' 的最少操作次数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
