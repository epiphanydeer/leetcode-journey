# 648. 单词替换
'''
在英语中，我们有一个叫做 词根(root) 的概念，可以词根 后面 添加其他一些词组成另一个较长的单词——我们称这个词为 衍生词 (derivative)。例如，词根 help，跟随着 继承词 "ful"，可以形成新的单词 "helpful"。

现在，给定一个由许多 词根 组成的词典 dictionary 和一个用空格分隔单词形成的句子 sentence。你需要将句子中的所有 衍生词 用 词根 替换掉。如果 衍生词 有许多可以形成它的 词根，则用 最短 的 词根 替换它。

你需要输出替换之后的句子。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
