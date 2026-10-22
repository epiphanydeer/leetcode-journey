# 88. 合并两个有序数组
"""
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
【解题思路】
1. 要往nums1里面填数字，那就倒序填入
2. nums2的每个数去和num1的数字比大小，大的先放
3. 用写指针去按位置填入数字
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 考虑越界和停止的问题，得等nums2的数全放进去才能停，会遇到三种情况
        # 1. nums2的比nums1的多，那就等nums2全放完就结束，Nums2和nums1一样多，那也是Nums2先放完
        # nums2的个数小于Nums1，那放完nums2也结束了，因为nums1本来就排好的
        # 所以，Nums2放完就结束。
        n2 = len(nums2)
        left, right = m - 1, n2 - 1
        write = m + n - 1
        # 考虑边界问题，right = 0的时候放不放？要放，当right = 0才放最后一个数
        while right >= 0:
            # 再考虑left的边界问题，nums2比nums1多的时候，nums1放完就放完，剩下的位置就Nums2排序放
            if left >= 0 and nums1[left] > nums2[right]:
                nums1[write] = nums1[left]
                left -= 1
            else:
                # left < 0 的时候，数小的时候，就全放right
                nums1[write] = nums2[right]
                right -= 1
            write -= 1
        return nums1


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
