# 3827. 统计单比特整数
'''
给你一个整数 n。

如果一个整数的二进制表示中所有位都相同，则称其为 单比特数（Monobit）。

返回范围[0, n]（包括两端）内 单比特数 的个数。

 

示例 1：

输入： n = 1

输出： 2

解释：

 范围[0, 1]内的整数对应的二进制表示为"0"和"1"。

 每个表示都由相同的位组成，因此答案是2。

示例 2：

输入： n = 4

输出： 3

解释：

 范围[0, 4]内的整数对应的二进制表示为"0"、"1"、"10"、"11"和"100"。

 只有0、1和3满足单比特条件。因此答案是3。

 

提示：

 0 <= n <= 1000
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countMonobit(self, n):
        """
        :type n: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
