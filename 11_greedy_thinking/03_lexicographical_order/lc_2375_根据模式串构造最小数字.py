# 2375. 根据模式串构造最小数字
'''
给你下标从 0 开始、长度为 n 的字符串 pattern ，它包含两种字符，'I' 表示 上升 ，'D' 表示 下降 。

你需要构造一个下标从 0 开始长度为 n + 1 的字符串，且它要满足以下条件：

 num 包含数字 '1' 到 '9' ，其中每个数字 至多 使用一次。

 如果 pattern[i] == 'I' ，那么 num[i] < num[i + 1] 。

 如果 pattern[i] == 'D' ，那么 num[i] > num[i + 1] 。

请你返回满足上述条件字典序 最小 的字符串 num。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
