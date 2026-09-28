# 3939. 统计有根树中不相邻子集的数目
'''
给你一棵有 n 个节点的有根树，节点编号从 0 到 n - 1 ，由一个长度为 n 的整数数组 parent 表示，其中：

 parent[0] = -1 （节点 0 是根节点）。

 对于每个 1 <= i < n ，parent[i] 是节点 i 的父节点（0 <= parent[i] < i）。

另外给你一个长度为 n 的整数数组 nums ，其中 nums[i] 是节点 i 的值，以及一个整数 k。

如果节点的一个非空子集满足以下条件，则称为 有效 子集：

 所选节点的值之 和 可以被 k 整除 。

 所选节点中没有 两 个节点在树中是 相邻 的（即没有节点及其直接父节点同时包含在子集中）。

返回有效子集的数量对 109 + 7 取余的结果。

 

示例 1：

输入： parent = [-1,0,1], nums = [1,2,3], k = 3

输出： 1

解释：

唯一有效的子集是 {2} 。它包含值为 3 的节点 2，可以被 3 整除。

示例 2：

输入： parent = [-1,0,0,0], nums = [2,1,2,1], k = 3

输出： 2

解释：

有效的子集有：

 {1, 2}：节点 1 和 2 都是节点 0 的子节点，且彼此不直接相连。它们的值之和为 1 + 2 = 3 ，可以被 3 整除。

 {2, 3}：节点 2 和 3 也不相邻。它们的值之和为 2 + 1 = 3 ，可以被 3 整除。

没有其他子集同时满足两个条件。因此，答案是 2 。

 

提示：

 n == parent.length == nums.length

 1 <= n <= 1000

 parent[0] == -1

 对于所有的 1 <= i < n：
 
 0 <= parent[i] < i

 
 

 1 <= nums[i] <= 109

 1 <= k <= 100​​​​​​​​​​​​​​

 parent 表示一棵有效的有根树。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countValidSubsets(self, parent, nums, k):
        """
        :type parent: List[int]
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
