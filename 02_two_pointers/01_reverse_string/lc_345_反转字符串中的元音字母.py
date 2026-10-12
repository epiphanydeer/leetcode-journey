# 345. 反转字符串中的元音字母
"""
给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。

元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现不止一次。
示例 1：
输入：s = "IceCreAm"
输出："AceCreIm"
解释：
s 中的元音是 ['I', 'e', 'e', 'A']。反转这些元音，s 变为 "AceCreIm".
示例 2：
输入：s = "leetcode"
输出："leotcede"
提示：
 1 <= s.length <= 3 * 105
 s 由 可打印的 ASCII 字符组成
 【解题思路】
 1. 判断是不是元音是就换
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right = 0, len(s) - 1
        s = list(s)
        while left < right:
            while left < right and s[left].lower() not in "aeiou":
                left += 1
            while left < right and s[right].lower() not in "aeiou":
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseVowels(s="IceCreAm"))
