# 2525. 根据规则将箱子分类
'''
给你四个整数 length ，width ，height 和 mass ，分别表示一个箱子的三个维度和质量，请你返回一个表示箱子 类别 的字符串。

 如果满足以下条件，那么箱子是 "Bulky" 的：

 
 箱子 至少有一个 维度大于等于 104 。

 或者箱子的 体积 大于等于 109 。

 
 

 如果箱子的质量大于等于 100 ，那么箱子是 "Heavy" 的。

 如果箱子同时是 "Bulky" 和 "Heavy" ，那么返回类别为 "Both" 。

 如果箱子既不是 "Bulky" ，也不是 "Heavy" ，那么返回类别为 "Neither" 。

 如果箱子是 "Bulky" 但不是 "Heavy" ，那么返回类别为 "Bulky" 。

 如果箱子是 "Heavy" 但不是 "Bulky" ，那么返回类别为 "Heavy" 。

注意，箱子的体积等于箱子的长度、宽度和高度的乘积。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
