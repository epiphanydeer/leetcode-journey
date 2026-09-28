# 972. 相等的有理数
'''
给定两个字符串 s 和 t ，每个字符串代表一个非负有理数，只有当它们表示相同的数字时才返回 true 。字符串中可以使用括号来表示有理数的重复部分。

有理数 最多可以用三个部分来表示：整数部分 <IntegerPart>、小数非重复部分 <NonRepeatingPart> 和小数重复部分 <(><RepeatingPart><)>。数字可以用以下三种方法之一来表示：

 <IntegerPart> 

 
 例： 0 ,12 和 123 

 
 

 <IntegerPart><.><NonRepeatingPart>
 
 例： 0.5 , 1. , 2.12 和 123.0001

 
 

 <IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)> 
 
 例： 0.1(6) ， 1.(9)， 123.00(1212)

 
 

十进制展开的重复部分通常在一对圆括号内表示。例如：

 1 / 6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66)
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def isRationalEqual(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
