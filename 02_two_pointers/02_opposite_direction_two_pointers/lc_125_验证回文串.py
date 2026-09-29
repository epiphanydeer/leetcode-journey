# 125. 验证回文串
"""
如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。

字母和数字都属于字母数字字符。

给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
【解题思路】
1. 如果是非字母数字字符，就跳过，是字母就判断
2. .lower()转化小写之后，俩指针开始判断是否一致，全程一致就return true
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(s="race a car"))
