# 844. 比较含退格的字符串
"""
给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。
【解题思路】
1. 因为遇到#是删除前一个元素，所以得倒着填，遇到#了，就跳一下
2. 可以维护一个skip变量，遇到#加一，然后遇到字母就看skip是几
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        left, right = len(s) - 1, len(t) - 1
        skip_s, skip_t = 0, 0
        while left >= 0 or right >= 0:
            while left >= 0:
                if s[left] == "#":
                    skip_s += 1
                    left -= 1
                elif skip_s > 0:
                    left -= 1
                    skip_s -= 1
                else:
                    break
            while right >= 0:
                if t[right] == "#":
                    skip_t += 1
                    right -= 1
                elif skip_t > 0:
                    right -= 1
                    skip_t -= 1
                else:
                    break
            if left >= 0 and right >= 0:
                if s[left] != t[right]:
                    return False
            elif left >= 0 or right >= 0:
                return False
            left -= 1
            right -= 1
        return True


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.backspaceCompare(s="bxj##tw", t="bxj###tw"))
