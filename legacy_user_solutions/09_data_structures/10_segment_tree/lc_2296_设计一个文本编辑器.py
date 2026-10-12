# 2296. 设计一个文本编辑器
'''
请你设计一个带光标的文本编辑器，它可以实现以下功能：

 添加：在光标所在处添加文本。

 删除：在光标所在处删除文本（模拟键盘的删除键）。

 移动：将光标往左或者往右移动。

当删除文本时，只有光标左边的字符会被删除。光标会留在文本内，也就是说任意时候 0 <= cursor.position <= currentText.length 都成立。

请你实现 TextEditor 类：

 TextEditor() 用空文本初始化对象。

 void addText(string text) 将 text 添加到光标所在位置。添加完后光标在 text 的右边。

 int deleteText(int k) 删除光标左边 k 个字符。返回实际删除的字符数目。

 string cursorLeft(int k) 将光标向左移动 k 次。返回移动后光标左边 min(10, len) 个字符，其中 len 是光标左边的字符数目。

 string cursorRight(int k) 将光标向右移动 k 次。返回移动后光标左边 min(10, len) 个字符，其中 len 是光标左边的字符数目。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class TextEditor(object):

    def __init__(self):
        

    def addText(self, text):
        """
        :type text: str
        :rtype: None
        """
        

    def deleteText(self, k):
        """
        :type k: int
        :rtype: int
        """
        

    def cursorLeft(self, k):
        """
        :type k: int
        :rtype: str
        """
        

    def cursorRight(self, k):
        """
        :type k: int
        :rtype: str
        """
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
