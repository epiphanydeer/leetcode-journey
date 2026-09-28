# 2019. 解出数学表达式的学生分数
'''
给你一个字符串 s ，它 只 包含数字 0-9 ，加法运算符 '+' 和乘法运算符 '*' ，这个字符串表示一个 合法 的只含有 个位数数字 的数学表达式（比方说 3+5*2）。有 n 位小学生将计算这个数学表达式，并遵循如下 运算顺序 ：

 按照 从左到右 的顺序计算 乘法 ，然后

 按照 从左到右 的顺序计算 加法 。

给你一个长度为 n 的整数数组 answers ，表示每位学生提交的答案。你的任务是给 answer 数组按照如下 规则 打分：

 如果一位学生的答案 等于 表达式的正确结果，这位学生将得到 5 分。

 否则，如果答案由 一处或多处错误的运算顺序 计算得到，那么这位学生能得到 2 分。

 否则，这位学生将得到 0 分。

请你返回所有学生的分数和。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def scoreOfStudents(self, s, answers):
        """
        :type s: str
        :type answers: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
