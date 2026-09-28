# 1441. 用栈操作构建数组
'''
给你一个数组 target 和一个整数 n。

给你一个空栈和两种操作：

 "Push"：将一个整数加到栈顶。

 "Pop"：从栈顶删除一个整数。

同时给定一个范围 [1, n] 中的整数流。

使用两个栈操作使栈中的数字（从底部到顶部）等于 target。你应该遵循以下规则：

 如果整数流不为空，从流中选取下一个整数并将其推送到栈顶。

 如果栈不为空，弹出栈顶的整数。

 如果，在任何时刻，栈中的元素（从底部到顶部）等于 target，则不要从流中读取新的整数，也不要对栈进行更多操作。

请返回遵循上述规则构建 target 所用的操作序列。如果存在多个合法答案，返回 任一 即可。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
