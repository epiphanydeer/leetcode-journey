# 04. Monotonic Stack / 03_contribution

## 解题记录

- 题号与链接：
- 核心思路：
- 不变量 / 状态定义：
- 时间复杂度：
- 空间复杂度：
- 边界用例：

## Python 起手模板

```python
def solve(nums):
    stack = []  # store indices; keep the chosen monotonic order
    for i, value in enumerate(nums):
        while stack and nums[stack[-1]] <= value:  # adjust the relation
            previous = stack.pop()
            # settle previous using i as its next boundary
        stack.append(i)
```