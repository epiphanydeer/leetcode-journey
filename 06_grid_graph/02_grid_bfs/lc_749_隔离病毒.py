# 749. 隔离病毒
'''
病毒扩散得很快，现在你的任务是尽可能地通过安装防火墙来隔离病毒。

假设世界由 m x n 的二维矩阵 isInfected 组成， isInfected[i][j] == 0 表示该区域未感染病毒，而  isInfected[i][j] == 1 表示该区域已感染病毒。可以在任意 2 个相邻单元之间的共享边界上安装一个防火墙（并且只有一个防火墙）。

每天晚上，病毒会从被感染区域向相邻未感染区域扩散，除非被防火墙隔离。现由于资源有限，每天你只能安装一系列防火墙来隔离其中一个被病毒感染的区域（一个区域或连续的一片区域），且该感染区域对未感染区域的威胁最大且 保证唯一 。

你需要努力使得最后有部分区域不被病毒感染，如果可以成功，那么返回需要使用的防火墙个数; 如果无法实现，则返回在世界被病毒全部感染时已安装的防火墙个数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def containVirus(self, isInfected):
        """
        :type isInfected: List[List[int]]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
