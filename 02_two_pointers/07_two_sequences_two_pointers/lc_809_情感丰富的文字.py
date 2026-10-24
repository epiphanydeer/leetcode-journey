# 809. 情感丰富的文字
"""
有时候人们会用重复写一些字母来表示额外的感受，比如 "hello" -> "heeellooo", "hi" -> "hiii"。我们将相邻字母都相同的一串字符定义为相同字母组，例如："h", "eee", "ll", "ooo"。
对于一个给定的字符串 S ，如果另一个单词能够通过将一些字母组扩张从而使其和 S 相同，我们将这个单词定义为可扩张的（stretchy）。扩张操作定义如下：选择一个字母组（包含字母 c ），然后往其中添加相同的字母 c 使其长度达到 3 或以上。
例如，以 "hello" 为例，我们可以对字母组 "o" 扩张得到 "hellooo"，但是无法以同样的方法得到 "helloo" 因为字母组 "oo" 长度小于 3。此外，我们可以进行另一种扩张 "ll" -> "lllll" 以获得 "helllllooo"。如果 s = "helllllooo"，那么查询词 "hello" 是可扩张的，因为可以对它执行这两种扩张操作使得 query = "hello" -> "hellooo" -> "helllllooo" = s。
输入一组查询单词，输出其中可扩张的单词数量。
【解题思路】
1. 画逻辑图，首先大判断，如果不相等就break，相等了再继续
2.相等的前提下，统计俩的重复数量，不合格的情况：cnt1数量小于cnt2，cnt1数量大于cnt2但是次数小于3次
3. 合格的情况，cnt1数量小于3且等于cnt2，cnt1数量大于3了并且大于cnt2
4. 最后再判断是否都走到底了，没走到说明有不同的字母了
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def expressiveWords(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        for i in words:
            left, right = 0, 0
            while left < len(s) and right < len(i):
                if s[left] != i[right]:
                    break
                ch1 = s[left]
                cnt1 = 0
                while left < len(s) and ch1 == s[left]:
                    cnt1 += 1
                    left += 1
                cnt2 = 0
                ch2 = i[right]
                while right < len(i) and ch2 == i[right]:
                    cnt2 += 1
                    right += 1
                if cnt1 < cnt2 or (cnt1 > cnt2 and cnt1 < 3):
                    break
            else:
                # 要判断走到底
                if left == len(s) and right == len(i):
                    ans += 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.expressiveWords(s="heeellooo", words=["hello", "hi", "helo"]))
