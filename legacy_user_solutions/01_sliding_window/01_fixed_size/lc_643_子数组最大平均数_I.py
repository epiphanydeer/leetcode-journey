# 643. 子数组最大平均数 I
"""
给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。
请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。
任何误差小于 10^-5 的答案都将被视为正确答案。

【核心思路】
1. 固定滑块，left固定，只需要确定最大值，return平均数即可
"""

from typing import List  # noqa: UP035


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = crt = 0
        for right, x in enumerate(nums):
            crt += x
            left = right - k + 1
            if left < 0:
                continue
            ans = max(ans, crt)
            crt -= nums[left]
            left += 1
        return ans / k


if __name__ == "__main__":
    solution = Solution()
    output = solution.findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4)
    print(f" Result: {output}")
