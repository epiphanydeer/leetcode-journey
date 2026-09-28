# 1249. 移除无效的括号
'''
给你一个由 '('、')' 和小写字母组成的字符串 s。

你需要从字符串中删除最少数目的 '(' 或者 ')' （可以删除任意位置的括号)，使得剩下的「括号字符串」有效。

请返回任意一个合法字符串。

有效「括号字符串」应当符合以下 任意一条 要求：

 空字符串或只包含小写字母的字符串

 可以被写作 AB（A 连接 B）的字符串，其中 A 和 B 都是有效「括号字符串」

 可以被写作 (A) 的字符串，其中 A 是一个有效的「括号字符串」
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
