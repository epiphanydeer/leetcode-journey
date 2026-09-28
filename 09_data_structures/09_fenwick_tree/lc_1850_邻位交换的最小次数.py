# 1850. 邻位交换的最小次数
'''
给你一个表示大整数的字符串 num ，和一个整数 k 。

如果某个整数是 num 中各位数字的一个 排列 且它的 值大于 num ，则称这个整数为 妙数 。可能存在很多妙数，但是只需要关注 值最小 的那些。

 例如，num = "5489355142" ：

 
 第 1 个最小妙数是 "5489355214"

 第 2 个最小妙数是 "5489355241"

 第 3 个最小妙数是 "5489355412"

 第 4 个最小妙数是 "5489355421"

 
 

返回要得到第 k 个 最小妙数 需要对 num 执行的 相邻位数字交换的最小次数 。

测试用例是按存在第 k 个最小妙数而生成的。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def getMinSwaps(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
