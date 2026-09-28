# 690. 员工的重要性
'''
你有一个保存员工信息的数据结构，它包含了员工唯一的 id ，重要度和直系下属的 id 。

给定一个员工数组 employees，其中：

 employees[i].id 是第 i 个员工的 ID。

 employees[i].importance 是第 i 个员工的重要度。

 employees[i].subordinates 是第 i 名员工的直接下属的 ID 列表。

给定一个整数 id 表示一个员工的 ID，返回这个员工和他所有下属的重要度的 总和。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
