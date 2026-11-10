# 1760. 袋子里最少数目的球
"""
给你一个整数数组 nums ，其中 nums[i] 表示第 i 个袋子里球的数目。同时给你一个整数 maxOperations 。

你可以进行如下操作至多 maxOperations 次：

 选择任意一个袋子，并将袋子里的球分到 2 个新的袋子中，每个袋子里都有 正整数 个球。


 比方说，一个袋子里有 5 个球，你可以把它们分到两个新袋子里，分别有 1 个和 4 个球，或者分别有 2 个和 3 个球。
你的开销是单个袋子里球数目的 最大值 ，你想要 最小化 开销。

请你返回进行上述操作后的最小开销。
【解题思路】
1. 人话就是最小化每个袋子的球，拆分次数越少 maxNumber 越大，次数越多 maxNumber 越小。
2. 直接去看最后，maxoperations后每个袋子球是多少
3. 一个原本装有x个球的袋子，如果每袋最多装mid个球，最少需要切几刀（操作几次）
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """

        def check(mid: int) -> bool:
            total = 0
            for i in nums:
                total += (i + mid - 1) // mid - 1
                # 等价于 (i - 1)// mid
            return total <= maxOperations

        left, right = 1, max(nums)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumSize(nums=[9], maxOperations=2))
    print(solution.minimumSize(nums=[2, 4, 8, 2], maxOperations=4))
    print(solution.minimumSize(nums=[7, 17], maxOperations=2))
