# 2306. 公司命名
'''
给你一个字符串数组 ideas 表示在公司命名过程中使用的名字列表。公司命名流程如下：

 从 ideas 中选择 2 个 不同 名字，称为 ideaA 和 ideaB 。

 交换 ideaA 和 ideaB 的首字母。

 如果得到的两个新名字 都 不在 ideas 中，那么 ideaA ideaB（串联 ideaA 和 ideaB ，中间用一个空格分隔）是一个有效的公司名字。

 否则，不是一个有效的名字。

返回 不同 且有效的公司名字的数目。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def distinctNames(self, ideas):
        """
        :type ideas: List[str]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
