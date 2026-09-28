# 745. 前缀和后缀搜索
'''
设计一个包含一些单词的特殊词典，并能够通过前缀和后缀来检索单词。

实现 WordFilter 类：

 WordFilter(string[] words) 使用词典中的单词 words 初始化对象。

 f(string pref, string suff) 返回词典中具有前缀 pref 和后缀 suff 的单词的下标。如果存在不止一个满足要求的下标，返回其中 最大的下标 。如果不存在这样的单词，返回 -1 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        

    def f(self, pref, suff):
        """
        :type pref: str
        :type suff: str
        :rtype: int
        """
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
