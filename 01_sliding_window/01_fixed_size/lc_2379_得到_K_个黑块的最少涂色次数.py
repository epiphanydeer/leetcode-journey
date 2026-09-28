# 2379. 得到 K 个黑块的最少涂色次数
"""
给你一个长度为 n 下标从 0 开始的字符串 blocks ，blocks[i] 要么是 'W' 要么是 'B' ，表示第 i 块的颜色。字符 'W' 和 'B' 分别表示白色和黑色。
给你一个整数 k ，表示想要 连续 黑色块的数目。
每一次操作中，你可以选择一个白色块将它 涂成 黑色块。
请你返回至少出现 一次 连续 k 个黑色块的 最少 操作次数。

【核心思路】
1. 反向思考，也就是找最大连续的黑块，里面白块数目最少，
所以题目变为，找固定块，白色最少，
因此ans应该是min()所以ans得初始值设置大一点
2. 定长块，不考虑左指针
"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans, crt = len(blocks), 0
        for right, x in enumerate(blocks):
            left = right - k + 1
            if x == "W":
                crt += 1
            if left < 0:
                continue
            ans = min(ans, crt)
            if blocks[left] == "W":
                crt -= 1
            left += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    output = solution.minimumRecolors(blocks="WBBWWBBWBW", k=7)
    print(f" Result: {output}")
