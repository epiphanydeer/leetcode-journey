# 1343. 大小为 K 且平均值大于等于阈值的子数组数目
"""
给你一个整数数组 arr 和两个整数 k 和 threshold 。
请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。

【核心思路】

"""

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = crt = 0
        for right, x in enumerate(arr):
            left = right - k + 1
            crt += x
            if left < 0:
                continue
            if crt >= k * threshold:
                ans += 1
            crt -= arr[left]
            left += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    output = solution.numOfSubarrays(arr=[2, 2, 2, 2, 5, 5, 5, 8], k=3, threshold=4)
    print(f" Result: {output}")
