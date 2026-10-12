# 2469. 温度转换
'''
给你一个四舍五入到两位小数的非负浮点数 celsius 来表示温度，以 摄氏度（Celsius）为单位。

你需要将摄氏度转换为 开氏度（Kelvin）和 华氏度（Fahrenheit），并以数组 ans = [kelvin, fahrenheit] 的形式返回结果。

返回数组 ans 。与实际答案误差不超过 10-5 的会视为正确答案。

注意：

 开氏度 = 摄氏度 + 273.15

 华氏度 = 摄氏度 * 1.80 + 32.00
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
