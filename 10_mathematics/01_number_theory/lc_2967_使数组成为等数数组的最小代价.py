# 2967. 使数组成为等数数组的最小代价
'''
给你一个整数数组 nums。

在一次 操作 中，你可以选择一个下标 i，并将 nums[i] 加 1 或减 1。

返回将 nums 中每个元素都变为 相同 的 正回文整数 所需的 最小 操作数。

 

示例 1：

输入：nums = [1,2,3,4,5]
输出：6
解释：增加 nums[0] 两次和 nums[1] 一次，然后减少 nums[3] 一次和 nums[4] 两次。经过 6 次操作，nums 变为 [3,3,3,3,3]，3 是一个正回文整数。
可以证明这是所需的最小操作次数。

示例 2：

输入：nums = [10,12,13,14,15]
输出：11
解释：增加 nums[0] 一次，然后分别减少 nums[1]、nums[2]、nums[3] 和 nums[4] 1、2、3 和 4 次。经过 11 次操作后，nums 变为 [11,11,11,11,11]，11 是一个正回文整数。
可以证明这是所需的最小操作次数。

示例 3 ：

输入：nums = [22,33,22,33,22]
输出：22
解释：减少 nums[1] 和 nums[3] 各 11 次。经过 22 次操作，nums 变为 [22,22,22,22,22]，22 是一个正回文整数。
可以证明这是所需的最小操作次数。

 

提示：

 1 <= n <= 105

 1 <= nums[i] <= 109
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
