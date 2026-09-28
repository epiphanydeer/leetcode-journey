# 1111. 有效括号的嵌套深度
'''
如果一个字符串仅由字符 "(" 和 ")" 组成，并且满足以下条件，则称为有效括号字符串（VPS）：

 它是空字符串，或

 它可以表示为 AB（A 连接 B），其中 A 和 B 都是VPS，或者

 它可以表示为 (A)，其中 A 是一个 VPS。

我们可以类似地定义任何 VPS S 的嵌套深度 depth(S) 如下：

 depth("") = 0

 depth(A + B) = max(depth(A), depth(B))，其中 A 和 B 都是 VPS

 depth("(" + A + ")") = 1 + depth(A)，其中 A 是一个 VPS。

例如，""，"()()" 和 "()(()())" 都是 VPS（嵌套深度 0，1 和 2），并且 ")(" 和 "(()" 不是 VPS。

给定一个 VPS 序列，将其拆分成两个不相交的子序列 A 和 B，使得 A 和 B 都是 VPS（且 A.length + B.length = seq.length）。这些子序列不一定是连续的。

例如，对于序列 123456789，一种可能的拆分是：

 
 A = {1, 3, 5, 7, 9}，

 

 
 B = {2, 4, 6, 8}。

 

 
 这对应于输出 [0, 1, 0, 1, 0, 1, 0, 1, 0]，其中 0 表示属于 A，1 表示属于 B。

 

现在选择 任意 这样的 A 和 B，使得 max(depth(A), depth(B)) 的值是最小的。

返回一个 answer 数组（长度为 seq.length），该数组编码了 A 和 B 的选择：如果 seq[i] 是 A 的一部分则 answer[i] = 0，否则 answer[i] = 1。请注意，尽管可能存在多种答案，但你可以返回其中任意一种。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
