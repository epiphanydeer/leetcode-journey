# 1157. 子数组中占绝大多数的元素
'''
设计一个数据结构，有效地找到给定子数组的 多数元素 。

子数组的 多数元素 是在子数组中出现 threshold 次数或次数以上的元素。

实现 MajorityChecker 类:

 MajorityChecker(int[] arr) 会用给定的数组 arr 对 MajorityChecker 初始化。

 int query(int left, int right, int threshold) 返回子数组中的元素  arr[left...right] 至少出现 threshold 次数，如果不存在这样的元素则返回 -1。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class MajorityChecker(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        

    def query(self, left, right, threshold):
        """
        :type left: int
        :type right: int
        :type threshold: int
        :rtype: int
        """
        


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
