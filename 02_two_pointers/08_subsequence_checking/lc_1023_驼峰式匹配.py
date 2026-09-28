# 1023. 驼峰式匹配
'''
给你一个字符串数组 queries，和一个表示模式的字符串 pattern，请你返回一个布尔数组 answer 。只有在待查项 queries[i] 与模式串 pattern 匹配时， answer[i] 才为 true，否则为 false。

如果可以将 小写字母 插入模式串 pattern 得到待查询项 queries[i]，那么待查询项与给定模式串匹配。您可以在模式串中的任何位置插入字符，也可以选择不插入任何字符。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
