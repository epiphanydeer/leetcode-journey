# 848. 字母移位
'''
有一个由小写字母组成的字符串 s，和一个长度相同的整数数组 shifts。

我们将字母表中的下一个字母称为原字母的 移位 shift() （由于字母表是环绕的， 'z' 将会变成 'a'）。

 例如，shift('a') = 'b', shift('t') = 'u', 以及 shift('z') = 'a'。

对于每个 shifts[i] = x ， 我们会将 s 中的前 i + 1 个字母移位 x 次。

返回 将所有这些移位都应用到 s 后最终得到的字符串 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
