# 855. 考场就座
'''
在考场里，有 n 个座位排成一行，编号为 0 到 n - 1。

当学生进入考场后，他必须坐在离最近的人最远的座位上。如果有多个这样的座位，他会坐在编号最小的座位上。(另外，如果考场里没有人，那么学生就坐在 0 号座位上。)

设计一个模拟所述考场的类。

实现 ExamRoom 类：

 ExamRoom(int n) 用座位的数量 n 初始化考场对象。

 int seat() 返回下一个学生将会入座的座位编号。

 void leave(int p) 指定坐在座位 p 的学生将离开教室。保证座位 p 上会有一位学生。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class ExamRoom(object):

    def __init__(self, n):
        """
        :type n: int
        """
        

    def seat(self):
        """
        :rtype: int
        """
        

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
