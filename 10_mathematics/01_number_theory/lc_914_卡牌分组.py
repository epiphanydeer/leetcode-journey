# 914. 卡牌分组
'''
给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

 每组都有 X 张牌。

 组内所有的牌上都写着相同的整数。

仅当你可选的 X >= 2 时返回 true。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
