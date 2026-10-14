# 1255. 得分最高的单词集合
'''
你将会得到一份单词表 words，一个字母表 letters （可能会有重复字母），以及每个字母对应的得分情况表 score。

请你帮忙计算玩家在单词拼写游戏中所能获得的「最高得分」：能够由 letters 里的字母拼写出的 任意 属于 words 单词子集中，分数最高的单词集合的得分。

单词拼写游戏的规则概述如下：

 玩家需要用字母表 letters 里的字母来拼写单词表 words 中的单词。

 可以只使用字母表 letters 中的部分字母，但是每个字母最多被使用一次。

 单词表 words 中每个单词只能计分（使用）一次。

 根据字母得分情况表score，字母 'a', 'b', 'c', ... , 'z' 对应的得分分别为 score[0], score[1], ..., score[25]。

 本场游戏的「得分」是指：玩家所拼写出的单词集合里包含的所有字母的得分之和。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
