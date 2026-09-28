# 917. 仅仅反转字母
'''
给你一个字符串 s ，根据下述规则反转字符串：

 所有非英文字母保留在原有位置。

 所有英文字母（小写或大写）位置反转。

返回反转后的 s 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
