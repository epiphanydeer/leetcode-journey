# 486. 预测赢家
'''
给你一个整数数组 nums。

玩家 1 和玩家 2 基于这个数组设计了一个游戏。

玩家 1 和玩家 2 轮流进行自己的回合，玩家 1 先手。开始时，两个玩家的初始分值都是 0 。

每一回合，玩家从数组的 任意一端 取一个数字（即，nums[0] 或 nums[nums.length - 1]），取到的数字将会从数组中 移除（数组长度减 1 ）。玩家选中的数字将会加到他的得分上。当数组中没有剩余数字可取时，游戏结束。

如果玩家 1 能成为赢家，返回 true 。

注意，如果两个玩家得分相等，同样认为玩家 1 是游戏的赢家。你可以假设每个玩家的玩法都会使他的分数最大化。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
