# 843. 猜猜这个单词
'''
给你一个由 不同 字符串组成的单词列表 words ，其中 words[i] 长度均为 6 。words 中的一个单词将被选作秘密单词 secret 。

另给你一个辅助对象 Master ，你可以调用 Master.guess(word) 来猜单词，其中参数 word 长度为 6 且必须是 words 中的字符串。

Master.guess(word) 将会返回如下结果：

 如果 word 不是 words 中的字符串，返回 -1 ，或者

 一个整数，表示你所猜测的单词 word 与 秘密单词 secret 的准确匹配（值和位置同时匹配）的数目。

每组测试用例都会包含一个参数 allowedGuesses ，其中 allowedGuesses 是你可以调用 Master.guess(word) 的最大次数。

对于每组测试用例，在不超过允许猜测的次数的前提下，你应该调用 Master.guess 来猜出秘密单词。最终，你将会得到以下结果：

 如果你调用 Master.guess 的次数大于 allowedGuesses 所限定的次数或者你没有用 Master.guess 猜到秘密单词，则得到 "Either you took too many guesses, or you did not find the secret word." 。

 如果你调用 Master.guess 猜到秘密单词，且调用 Master.guess 的次数小于或等于 allowedGuesses ，则得到 "You guessed the secret word correctly." 。

生成的测试用例保证你可以利用某种合理的策略（而不是暴力）猜到秘密单词。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def findSecretWord(self, words, master):
        """
        :type words: List[Str]
        :type master: Master
        :rtype: None
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
