# 2554. 从一个范围内选择最多整数 I
'''
给你一个整数数组 banned 和两个整数 n 和 maxSum 。你需要按照以下规则选择一些整数：

 被选择整数的范围是 [1, n] 。

 每个整数 至多 选择 一次 。

 被选择整数不能在数组 banned 中。

 被选择整数的和不超过 maxSum 。

请你返回按照上述规则 最多 可以选择的整数数目。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
