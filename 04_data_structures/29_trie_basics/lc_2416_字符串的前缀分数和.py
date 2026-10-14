# 2416. 字符串的前缀分数和
'''
给你一个长度为 n 的数组 words ，该数组由 非空 字符串组成。

定义字符串 term 的 分数 等于以 term 作为 前缀 的 words[i] 的数目。

 例如，如果 words = ["a", "ab", "abc", "cab"] ，那么 "ab" 的分数是 2 ，因为 "ab" 是 "ab" 和 "abc" 的一个前缀。

返回一个长度为 n 的数组 answer ，其中 answer[i] 是 words[i] 的每个非空前缀的分数 总和 。

注意：字符串视作它自身的一个前缀。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
