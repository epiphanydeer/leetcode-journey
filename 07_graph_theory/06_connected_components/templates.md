# 07. Graph Theory / 06_connected_components

## 解题记录

- 题号与链接：
- 核心思路：
- 不变量 / 状态定义：
- 时间复杂度：
- 空间复杂度：
- 边界用例：

## Python 起手模板

```python
from collections import deque

def bfs(start, graph):
    queue = deque([start])
    visited = {start}
    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
```