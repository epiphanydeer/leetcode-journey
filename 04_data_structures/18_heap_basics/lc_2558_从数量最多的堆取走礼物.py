# 2558. 从数量最多的堆取走礼物
'''
给你一个整数数组 gifts ，表示各堆礼物的数量。每一秒，你需要执行以下操作：

 选择礼物数量最多的那一堆。

 如果不止一堆都符合礼物数量最多，从中选择任一堆即可。

 将堆中的礼物数量减少到堆中原来礼物数量的平方根，向下取整。

返回在 k 秒后剩下的礼物数量。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
