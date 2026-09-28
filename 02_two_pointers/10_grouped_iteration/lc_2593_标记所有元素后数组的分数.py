# 2593. 标记所有元素后数组的分数
'''
给你一个数组 nums ，它包含若干正整数。

一开始分数 score = 0 ，请你按照下面算法求出最后分数：

 从数组中选择最小且没有被标记的整数。如果有相等元素，选择下标最小的一个。

 将选中的整数加到 score 中。

 标记 被选中元素，如果有相邻元素，则同时标记 与它相邻的两个元素 。

 重复此过程直到数组中所有元素都被标记。

请你返回执行上述算法后最后的分数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
