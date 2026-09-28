# 1977. 划分数字的方案数
'''
你写下了若干 正整数 ，并将它们连接成了一个字符串 num 。但是你忘记给这些数字之间加逗号了。你只记得这一列数字是 非递减 的且 没有 任何数字有前导 0 。

请你返回有多少种可能的 正整数数组 可以得到字符串 num 。由于答案可能很大，将结果对 109 + 7 取余 后返回。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def numberOfCombinations(self, num):
        """
        :type num: str
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
