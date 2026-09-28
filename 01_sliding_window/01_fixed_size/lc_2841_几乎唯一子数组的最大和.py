# 2841. 几乎唯一子数组的最大和
"""
给你一个整数数组 nums 和两个正整数 m 和 k 。
请你返回 nums 中长度为 k 的 几乎唯一 子数组的 最大和 ，如果不存在几乎唯一子数组，请你返回 0 。
如果 nums 的一个子数组有至少 m 个互不相同的元素，我们称它是 几乎唯一 子数组。
子数组指的是一个数组中一段连续 非空 的元素序列。
示例 1：
输入：nums = [2,6,7,3,1,7], m = 3, k = 4
输出：18
解释：总共有 3 个长度为 k = 4 的几乎唯一子数组。分别为 [2, 6, 7, 3] ，[6, 7, 3, 1] 和 [7, 3, 1, 7] 。这些子数组中，和最大的是 [2, 6, 7, 3] ，和为 18 。
示例 2：
输入：nums = [5,9,9,2,4,5,4], m = 1, k = 3
输出：23
解释：总共有 5 个长度为 k = 3 的几乎唯一子数组。分别为 [5, 9, 9] ，[9, 9, 2] ，[9, 2, 4] ，[2, 4, 5] 和 [4, 5, 4] 。这些子数组中，和最大的是 [5, 9, 9] ，和为 23 。
示例 3：
输入：nums = [1,2,1,2,1,2,1], m = 3, k = 3
输出：0
解释：输入数组中不存在长度为 k = 3 的子数组含有至少 m = 3 个互不相同元素的子数组。所以不存在几乎唯一子数组，最大和为 0 。

【核心思路】
1. 固定块（题目说到了长度为k）
2. 提到了“几乎唯一”数字都不同，考虑使用defaultdict
3. 提到了至少m个不相同的，则len(defaultdict)，
"""

from collections import defaultdict
from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        d = defaultdict(int)
        ans, crt = 0, 0
        for right, x in enumerate(nums):
            crt += x
            left = right - k + 1
            d[x] += 1
            if left < 0:
                continue
            if len(d) >= m:
                ans = max(ans, crt)
            j = nums[left]
            crt -= j
            d[j] -= 1
            if d[j] == 0:
                del d[j]
            left += 1
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    output = solution.maxSum(nums=[2, 6, 7, 3, 1, 7], m=3, k=4)
    print(f" Result: {output}")
