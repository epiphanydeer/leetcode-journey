# 2102. 序列顺序查询
'''
一个观光景点由它的名字 name 和景点评分 score 组成，其中 name 是所有观光景点中 唯一 的字符串，score 是一个整数。景点按照最好到最坏排序。景点评分 越高 ，这个景点越好。如果有两个景点的评分一样，那么 字典序较小 的景点更好。

你需要搭建一个系统，查询景点的排名。初始时系统里没有任何景点。这个系统支持：

 添加 景点，每次添加 一个 景点。

 查询 已经添加景点中第 i 好 的景点，其中 i 是系统目前位置查询的次数（包括当前这一次）。
 
 比方说，如果系统正在进行第 4 次查询，那么需要返回所有已经添加景点中第 4 好的。

 
 

注意，测试数据保证 任意查询时刻 ，查询次数都 不超过 系统中景点的数目。

请你实现 SORTracker 类：

 SORTracker() 初始化系统。

 void add(string name, int score) 向系统中添加一个名为 name 评分为 score 的景点。

 string get() 查询第 i 好的景点，其中 i 是目前系统查询的次数（包括当前这次查询）。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class SORTracker(object):

    def __init__(self):
        

    def add(self, name, score):
        """
        :type name: str
        :type score: int
        :rtype: None
        """
        

    def get(self):
        """
        :rtype: str
        """
        


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
