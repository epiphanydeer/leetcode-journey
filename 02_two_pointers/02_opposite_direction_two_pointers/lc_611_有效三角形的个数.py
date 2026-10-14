# 611. 有效三角形的个数
"""
给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数。
【解题思路】
1. 要固定最长边，因为如果固定最短边，当left往右走，right往左走的时候，i + left + right会出现多种情况
比如：left往右走的时候，最右边的right也可能符合规则，指针就要回头，跟暴力解法没区别。
2. 计数的问题：如果left和right加起来大于第三边了，那说明从left到right-1的闭区间都是合适的，所以直接（right - 1 - left + 1），然后right -= 1
如果目前left和最大的right加起来都小于第三边，那剩下的right都带不动，就要left +=1 了
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(2, n):
            left, right = 0, i - 1
            while left < right:
                x = nums[i] - nums[left] - nums[right]
                if x >= 0:
                    left += 1
                else:
                    ans += right - left
                    right -= 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.triangleNumber(nums=[2, 2, 3, 4]))
