# 925. 长按键入
"""
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。

你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。
【解题思路】
1. 选name里面的一个字符，去和typed的对比
相同，就跳过，不相同，就判断是不是重复输入，看right和right-1是否相同，相同就+=1
2. 看边界条件，外围判断right，把typed遍历完
left的边界是如果left跑完了，right还没跑完并且后面还有不同字符的，返回错误
3. 记得边界条件，在写判断or循环看到里面有加减就要想是否超index了
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        n1 = len(name)
        n2 = len(typed)
        left, right = 0, 0
        while right < n2:
            if left < n1 and name[left] == typed[right]:
                left += 1
                right += 1
            elif right > 0 and typed[right] == typed[right - 1]:
                right += 1
            else:
                return False
        if left == n1:
            return True
        else:
            return False


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.isLongPressedName(name="alexd", typed="ale"))
