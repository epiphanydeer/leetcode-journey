# 01. 滑动窗口专题题单 (Sliding Window)

## 一、定长滑动窗口 (Fixed Size)
| 题号 | 题目 | 难度 | 题解 | 核心考点 |
| :---: | :--- | :---: | :---: | :--- |
| 1456 | [定长子串中元音的最大数目](https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) | Easy | [Python](./01_fixed_size/lc_1456_max_vowels.py) | 定长进出维护计数 |
| 438 | [找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) | Medium | [Python](./01_fixed_size/lc_438_find_anagrams.py) | 数组/哈希比对窗口状态 |

## 二、不定长滑动窗口（求最长）
| 题号 | 题目 | 难度 | 题解 | 核心考点 |
| :---: | :--- | :---: | :---: | :--- |
| 003 | [无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) | Medium | [Python](./02_variable_longest/lc_003_longest_substring.py) | 哈希集合去重收缩 |
| 904 | [水果成篮](https://leetcode.cn/problems/fruit-into-baskets/) | Medium | [Python](./02_variable_longest/lc_904_fruit_baskets.py) | 最多两种类别的不定长最长 |

## 三、不定长滑动窗口（求最短）
| 题号 | 题目 | 难度 | 题解 | 核心考点 |
| :---: | :--- | :---: | :---: | :--- |
| 209 | [长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/) | Medium | [Python](./03_variable_shortest/lc_209_min_size_subarray.py) | 大于等于 Target 连续收缩 |