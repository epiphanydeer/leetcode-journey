# 1750. 删除字符串两端相同字符后的最短长度
"""
给你一个只包含字符 'a'，'b' 和 'c' 的字符串 s ，你可以执行下面这个操作（5 个步骤）任意次：
 选择字符串 s 一个 非空 的前缀，这个前缀的所有字符都相同。
 选择字符串 s 一个 非空 的后缀，这个后缀的所有字符都相同。
 前缀和后缀在字符串中任意位置都不能有交集。
 前缀和后缀包含的所有字符都要相同。
 同时删除前缀和后缀。
请你返回对字符串 s 执行上面操作任意次以后（可能 0 次），能得到的 最短长度 。
【解题思路】
1. 题目人话意思是左右两边如果是相同的字符就开始删，不同就不能删
2. 所以在外循环就得写条件，只有相同才开始缩进
3. 内部循环也要一直while判断是否前后一致，不能只删一次就停止了，比如aaxxxxa的形式
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            c = s[left]
            while c == s[right] and left <= right:
                right -= 1
            while c == s[left] and left <= right:
                left += 1
        return right - left + 1


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumLength(s="aabccabba"))
