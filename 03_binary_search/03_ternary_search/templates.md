# 03. Binary Search / 03_ternary_search

## 解题记录

- 题号与链接：
- 核心思路：
- 不变量 / 状态定义：
- 时间复杂度：
- 空间复杂度：
- 边界用例：

## Python 起手模板

```python
def first_true(left, right):
    """Return the first x in [left, right] satisfying check(x)."""
    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left
```