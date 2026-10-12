# 557. 反转字符串中的单词 III
"""
给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
【解题思路】
1. 翻转句子里的每个单词，那就按空格分完以后，每个单词翻转
"""

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
        :type s: str
        :rtype: str
        """
        a = []
        for word in s.split(" "):
            word = word[::-1]
            a.append(word)
        return " ".join(a)


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseWords(s="Let's take LeetCode contest"))
