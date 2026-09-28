# 920. 播放列表的数量
'''
你的音乐播放器里有 n 首不同的歌，在旅途中，你计划听 goal 首歌（不一定不同，即，允许歌曲重复）。你将会按如下规则创建播放列表：

 每首歌 至少播放一次 。

 一首歌只有在其他 k 首歌播放完之后才能再次播放。

给你 n、goal 和 k ，返回可以满足要求的播放列表的数量。由于答案可能非常大，请返回对 109 + 7 取余 的结果。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def numMusicPlaylists(self, n, goal, k):
        """
        :type n: int
        :type goal: int
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
