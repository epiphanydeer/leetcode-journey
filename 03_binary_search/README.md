# 二分查找与二分答案全能笔记

---

## 一、 二分下标的本质：一切皆可转化为 `lower_bound`

有序数组上的二分查找，核心就在于寻找满足特定条件的**第一个分界点**。
采用**闭区间 `[left, right]`** 写法，循环结束时 `left` 永远指向目标位置。

### 1. 基础模板：`>= target` 与 `> target`

只需要改动一个符号（`<` 还是 `<=`），就能区分是否包含等于关系：

```python
# 1. 寻找第一个 >= target 的下标 (lower_bound)
def lower_bound(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1      # mid 太小，目标在右边
        else:
            right = mid - 1     # mid >= target，继续往左压
    return left

# 2. 寻找第一个 > target 的下标 (upper_bound / bisect_right)
def upper_bound(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1      # 哪怕相等也要跳过，去找严格大于的
        else:
            right = mid - 1
    return left
```

### 2. 四大变体的统一转换公式

通过单个 `lower_bound` 即可推导出全部 4 种区间查询要求：

| 目标查询需求 | 转换公式 | 意义说明 |
| :--- | :--- | :--- |
| **第一个 $\ge x$** | `lower_bound(x)` | 基础定义 |
| **第一个 $> x$** | `lower_bound(x + 1)` | 整数下，严格大于 $x$ 等价于大于等于 $x + 1$ |
| **最后一个 $< x$** | `lower_bound(x) - 1` | 第一个 $\ge x$ 的前一个位置 |
| **最后一个 $\le x$** | `lower_bound(x + 1) - 1` | 第一个 $> x$ 的前一个位置 |

---

## 二、 二分答案的核心概念

* **本质**：把“求最值”转化为“验证可行性”。
* **前提**：解空间存在**单调性**（单调递增或递减），使得整个区间被分成连贯的 `True` 和 `False` 两部分。
* **分界点**：
  * 求最小值（最小化）：`[False, False, ..., True, True]` $\to$ 找第一个 `True`。
  * 求最大值（最大化）：`[True, True, ..., False, False]` $\to$ 找最后一个 `True`。

---

## 三、 二分答案的所有变体模板

### 变体 1：求满足条件的最小值（求“最小”、或“最小化最大值”）
* **单调性**：数值越大约容易满足（`False ... True`）。
* **典型题目**：LeetCode 875 (爱吃香蕉的柯柯)、LeetCode 410 (分割数组的最大值)。

```python
def check(mid: int) -> bool:
    # 验证 mid 是否达标 / 可行
    ...

left, right = MIN_ANS, MAX_ANS
ans = right

while left <= right:
    mid = (left + right) // 2
    if check(mid):
        ans = mid        # mid 可行，尝试寻找更小的可行解
        right = mid - 1
    else:
        left = mid + 1   # mid 不可行，答案必须更大

return ans
```

---

### 变体 2：求满足条件的最大值（求“最大”、或“最大化最小值”）
* **单调性**：数值越小越容易满足（`True ... False`）。
* **典型题目**：LeetCode 1552 (两球之间的磁力)、LeetCode 2226 (每个小孩最多能分到多少糖果)。

```python
def check(mid: int) -> bool:
    # 验证 mid 是否达标 / 可行
    ...

left, right = MIN_ANS, MAX_ANS
ans = left

while left <= right:
    mid = (left + right) // 2
    if check(mid):
        ans = mid        # mid 可行，尝试寻找更大的可行解
        left = mid + 1
    else:
        right = mid - 1  # mid 不可行，答案必须更小

return ans
```

---

### 变体 3：浮点数二分（连续实数二分）
* **特点**：用于求实数最优解，没有整除和 `+1 / -1`，通过固定迭代次数或设定精度 $\epsilon$ 终止循环。
* **典型题目**：实数求根、最大平均值子段。

```python
left, right = MIN_FLOAT, MAX_FLOAT
eps = 1e-7

# 方式一：精度控制
while right - left > eps:
    mid = (left + right) / 2.0
    if check(mid):
        left = mid     # 或 right = mid，视单调性方向而定
    else:
        right = mid

# 方式二：固定迭代次数（迭代 100 次精度可达 2^-100，完全避免死循环）
for _ in range(100):
    mid = (left + right) / 2.0
    if check(mid):
        left = mid
    else:
        right = mid

return left
```

---

### 变体 4：第 K 小 / 第 K 大元素（计数判定型二分）
* **特点**：在值域上二分，`check` 函数变为“统计小于等于 $mid$ 的元素个数”。
* **典型题目**：LeetCode 378 (有序矩阵中第 K 小的元素)、LeetCode 668 (乘法表中第 k 小的数)。

```python
def count_less_or_equal(mid: int) -> int:
    # 统计整个结构中 <= mid 的元素总数
    ...

left, right = MIN_VAL, MAX_VAL
ans = right

while left <= right:
    mid = (left + right) // 2
    if count_less_or_equal(mid) >= k:
        ans = mid        # 数量够了，mid 可能偏大或刚好，尝试往小找
        right = mid - 1
    else:
        left = mid + 1   # 数量不够，说明 mid 太小了

return ans
```

---

## 四、 核心心法与贪心在二分中的角色

1. **二分骨架不变**：外层的 `while left <= right` 永远只需根据“变大更容易还是变小更容易”选择变体 1 或 变体 2。
2. **难点永远在 `check(mid)` 的实现**：
   * **贪心模拟（最常见）**：在限定上界为 $mid$ 的前提下，每一步都按眼下最省资源的方式选（例如吃香蕉、安排船装运），看能不能在规定步数内完成。
   * **滑动窗口 / 前缀和**：用于检验是否存在长度满足要求且总和 $\le mid$ 的子段。
   * **动态规划 (DP) / 图论**：用于处理具有复杂状态转移的可行性判定。