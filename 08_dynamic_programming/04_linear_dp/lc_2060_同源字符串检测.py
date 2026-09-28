# 2060. 同源字符串检测
'''
原字符串由小写字母组成，可以按下述步骤编码：

 任意将其 分割 为由若干 非空 子字符串组成的一个 序列 。

 任意选择序列中的一些元素（也可能不选择），然后将这些元素替换为元素各自的长度（作为一个数字型的字符串）。

 重新 顺次连接 序列，得到编码后的字符串。

例如，编码 "abcdefghijklmnop" 的一种方法可以描述为：

 将原字符串分割得到一个序列：["ab", "cdefghijklmn", "o", "p"] 。

 选出其中第二个和第三个元素并分别替换为它们自身的长度。序列变为 ["ab", "12", "1", "p"] 。

 重新顺次连接序列中的元素，得到编码后的字符串："ab121p" 。

给你两个编码后的字符串 s1 和 s2 ，由小写英文字母和数字 1-9 组成。如果存在能够同时编码得到 s1 和 s2 原字符串，返回 true ；否则，返回 false。

注意：生成的测试用例满足 s1 和 s2 中连续数字数不超过 3 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def possiblyEquals(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
