# 917. 仅仅反转字母
"""
给你一个字符串 s ，根据下述规则反转字符串：

 所有非英文字母保留在原有位置。

 所有英文字母（小写或大写）位置反转。

返回反转后的 s 。
【解题思路】
1. isalpha那就翻转，not isalpha就跳过，用双指针
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        ans = list(s)
        left, right = 0, n - 1
        while left < right:
            while left < right and not ans[left].isalpha():
                left += 1
            while left < right and not ans[right].isalpha():
                right -= 1
            ans[left], ans[right] = ans[right], ans[left]
            left += 1
            right -= 1
        return "".join(ans)


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseOnlyLetters(s="a-bC-dEf-ghIj"))
