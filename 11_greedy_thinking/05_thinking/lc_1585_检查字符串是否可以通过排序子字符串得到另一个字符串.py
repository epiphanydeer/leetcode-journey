# 1585. 检查字符串是否可以通过排序子字符串得到另一个字符串
'''
给你两个字符串 s 和 t ，请你通过若干次以下操作将字符串 s 转化成字符串 t ：

 选择 s 中一个 非空 子字符串并将它包含的字符就地 升序 排序。

比方说，对下划线所示的子字符串进行操作可以由 "14234" 得到 "12344" 。

如果可以将字符串 s 变成 t ，返回 true 。否则，返回 false 。

一个 子字符串 定义为一个字符串中连续的若干字符。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def isTransformable(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
