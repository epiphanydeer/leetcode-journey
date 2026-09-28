# 1047. 删除字符串中的所有相邻重复项
'''
给出由小写字母组成的字符串 s，重复项删除操作 会选择两个相邻且相同的字母，并删除它们。

在 s 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
