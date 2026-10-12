# 3936. 将 0 移到末尾的最少交换次数
"""
给你一个整数数组 nums 。
在一步操作中，你可以选择任意两个 不同 的下标 i 和 j 并交换 nums[i] 和 nums[j] 。
返回将所有 0 移动到数组末尾所需的 最少 操作次数。
示例 1：
输入： nums = [0,1,0,3,12]
输出： 2
解释：
我们执行以下交换操作：
 交换 nums[0] 和 nums[3] ，得到 nums = [3, 1, 0, 0, 12] 。
 交换 nums[2] 和 nums[4] ，得到 nums = [3, 1, 12, 0, 0] 。
因此，答案是 2 。
示例 2：
输入： nums = [0,1,0,2]
输出： 1
解释：
我们执行以下交换操作：
 交换 nums[0] 和 nums[3] ，得到 nums = [2, 1, 0, 0] 。
因此，答案是 1 。
示例 3：
输入： nums = [1,2,0]
输出： 0
解释：
数组已经满足条件。因此，不需要任何交换操作。
【解题思路】
1.就判断一下左指针是否是0，不是0那就移动左指针，右指针看是0 就左移右指针
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def minimumSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        ans = 0
        while left < right:
            if nums[left] != 0:
                left += 1
            elif nums[right] == 0:
                right -= 1
            else:
                ans += 1
                left += 1
                right -= 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumSwaps(nums=[1, 2, 0]))
