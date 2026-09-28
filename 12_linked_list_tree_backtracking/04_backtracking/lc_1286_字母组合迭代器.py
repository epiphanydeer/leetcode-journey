# 1286. 字母组合迭代器
'''
请你设计一个迭代器类 CombinationIterator ，包括以下内容：

 CombinationIterator(string characters, int combinationLength) 一个构造函数，输入参数包括：用一个 有序且字符唯一 的字符串 characters（该字符串只包含小写英文字母）和一个数字 combinationLength 。

 函数 next() ，按 字典序 返回长度为 combinationLength 的下一个字母组合。

 函数 hasNext() ，只有存在长度为 combinationLength 的下一个字母组合时，才返回 true
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        

    def next(self):
        """
        :rtype: str
        """
        

    def hasNext(self):
        """
        :rtype: bool
        """
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
