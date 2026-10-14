# 1089. 复写零
"""
给你一个长度固定的整数数组 arr ，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。

注意：请不要在超过该数组长度的位置写入元素。请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。
【解题思路】
1. 如果正着走，会覆盖后面的数字，所以要倒序开始写，先预测一下复写0的长度确定最后一个数字后再开始倒序
2. 原地修改数组，有元素要变多/扩展，正写基本都覆盖了
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        vitrual_len = 0
        n = len(arr)
        read, write = 0, n - 1
        while vitrual_len < n:
            if arr[read] == 0:
                vitrual_len += 2
            else:
                vitrual_len += 1
            read += 1
        read -= 1
        if vitrual_len == n + 1:
            arr[write] = 0
            read -= 1
            write -= 1
        while read >= 0:
            if arr[read] == 0:
                arr[write], arr[write - 1] = 0, 0
                write -= 2
                read -= 1
            else:
                arr[write] = arr[read]
                write -= 1
                read -= 1
        return arr


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.duplicateZeros(arr=[1, 0, 2, 3, 0, 4, 5, 0]))
