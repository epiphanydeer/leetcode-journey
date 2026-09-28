# 2422. 使用合并操作将数组转换为回文序列
'''
给定一个由正整数组成的数组 nums。

可以对阵列执行如下操作，次数不限：选择任意两个相邻的元素并用它们的和替换它们。例如，如果 nums = [1,2,3,1]，则可以应用一个操作使其变为 [1,5,1]。

返回将数组转换为回文序列所需的最小操作数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
