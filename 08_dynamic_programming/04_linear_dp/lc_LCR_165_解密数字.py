# LCR 165. 解密数字
'''
现有一串神秘的密文 ciphertext，经调查，密文的特点和规则如下：

 密文由非负整数组成

 数字 0-25 分别对应字母 a-z

请根据上述规则将密文 ciphertext 解密为字母，并返回共有多少种解密结果。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def crackNumber(self, ciphertext):
        """
        :type ciphertext: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
