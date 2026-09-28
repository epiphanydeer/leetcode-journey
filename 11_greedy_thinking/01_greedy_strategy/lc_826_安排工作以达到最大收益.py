# 826. 安排工作以达到最大收益
'''
你有 n 个工作和 m 个工人。给定三个数组： difficulty, profit 和 worker ，其中:

 difficulty[i] 表示第 i 个工作的难度，profit[i] 表示第 i 个工作的收益。

 worker[i] 是第 i 个工人的能力，即该工人只能完成难度小于等于 worker[i] 的工作。

每个工人 最多 只能安排 一个 工作，但是一个工作可以 完成多次 。

 举个例子，如果 3 个工人都尝试完成一份报酬为 $1 的同样工作，那么总收益为 $3 。如果一个工人不能完成任何工作，他的收益为 $0 。

返回 在把工人分配到工作岗位后，我们所能获得的最大利润 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
