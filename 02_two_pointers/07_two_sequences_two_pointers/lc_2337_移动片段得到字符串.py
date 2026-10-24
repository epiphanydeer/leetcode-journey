# 2337. 移动片段得到字符串
"""
给你两个字符串 start 和 target ，长度均为 n 。每个字符串 仅 由字符 'L'、'R' 和 '_' 组成，其中：
 字符 'L' 和 'R' 表示片段，其中片段 'L' 只有在其左侧直接存在一个 空位 时才能向 左 移动，而片段 'R' 只有在其右侧直接存在一个 空位 时才能向 右 移动。
 字符 '_' 表示可以被 任意 'L' 或 'R' 片段占据的空位。
如果在移动字符串 start 中的片段任意次之后可以得到字符串 target ，返回 true ；否则，返回 false 。
【解题思路】
1. 先不管_去看看字符都相同不，相同才继续
2. start的L下标一定大于target的，R一定小于target的才能移动
3. 特殊情况 ___ 和 __R，第一个走完了，第二个没走完
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        left, right = 0, 0
        while left < len(start) and right < len(target):
            while left < len(start) and start[left] == "_":
                left += 1
            while right < len(target) and target[right] == "_":
                right += 1
            if left < len(start) and right < len(target):
                if start[left] != target[right]:
                    return False
                if start[left] == "L" and left < right:
                    return False
                if start[left] == "R" and left > right:
                    return False
                left += 1
                right += 1
        while left < len(start):
            if start[left] != "_":
                return False
            left += 1
        while right < len(target):
            if target[right] != "_":
                return False
            right += 1
        return True


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.canChange(start="_L__R__R_", target="L______RR"))
