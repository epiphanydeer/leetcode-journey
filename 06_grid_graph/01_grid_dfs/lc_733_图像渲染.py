# 733. 图像渲染
'''
有一幅以 m x n 的二维整数数组表示的图画 image ，其中 image[i][j] 表示该图画的像素值大小。你也被给予三个整数 sr ,  sc 和 color 。你应该从像素 image[sr][sc] 开始对图像进行上色 填充 。

为了完成 上色工作：

 从初始像素开始，将其颜色改为 color。

 对初始坐标的 上下左右四个方向上 相邻且与初始像素的原始颜色同色的像素点执行相同操作。

 通过检查与初始像素的原始颜色相同的相邻像素并修改其颜色来继续 重复 此过程。

 当 没有 其它原始颜色的相邻像素时 停止 操作。

最后返回经过上色渲染 修改 后的图像 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
