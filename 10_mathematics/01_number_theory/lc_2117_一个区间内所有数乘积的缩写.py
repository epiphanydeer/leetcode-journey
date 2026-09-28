# 2117. 一个区间内所有数乘积的缩写
'''
给你两个正整数 left 和 right ，满足 left <= right 。请你计算 闭区间 [left, right] 中所有整数的 乘积 。

由于乘积可能非常大，你需要将它按照以下步骤 缩写 ：

 统计乘积中 后缀 0 的数目，并 移除 这些 0 ，将这个数目记为 C 。

 
 比方说，1000 中有 3 个后缀 0 ，546 中没有后缀 0 。

 
 

 将乘积中剩余数字的位数记为 d 。如果 d > 10 ，那么将乘积表示为 <pre>...<suf> 的形式，其中 <pre> 表示乘积最 开始 的 5 个数位，<suf> 表示删除后缀 0 之后 结尾的 5 个数位。如果 d <= 10 ，我们不对它做修改。
 
 比方说，我们将 1234567654321 表示为 12345...54321 ，但是 1234567 仍然表示为 1234567 。

 
 

 最后，将乘积表示为 字符串 "<pre>...<suf>eC" 。
 
 比方说，12345678987600000 被表示为 "12345...89876e5" 。

 
 

请你返回一个字符串，表示 闭区间 [left, right] 中所有整数 乘积 的 缩写 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def abbreviateProduct(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
