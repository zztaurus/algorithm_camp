
"""

https://leetcode-cn.com/problems/decode-ways/


给一个只含数字的非空字符串 s ，请计算并返回解码方法的总数.


"""


class Solution(object):

    def numDecodings(self, s):

        """
        对于字符串 s 的某个位置 i 而言，我们只关心「位置 i 自己能否形成独立 item 」和「位置 i 能够与上一位置（i-1）能否形成 item」，而不关心 i-1 之前的位置。


        对于0，无法独立形成item, 但却有可能和上一个位置联合形成一个有效的item


        状态定义：

            f[i]: 前i个字符的解码方案数。
​
        状态转移方程

            a = ord(str(s[i])) - ord('0')

            b = (ord(str(s[i - 1])) - ord('0')) * 10 + ord(str(s[i])) - ord('0')


            f[i]=f[i−1],1⩽a≤9
            f[i]=f[i−2],10⩽b⩽26
            f[i]=f[i−1]+f[i−2],1⩽a≤9,10⩽b⩽26

        时间复杂度: O(n)

        空间复杂度: O(n)
​
        """

        n = len(s)
        s = ' ' + s
        f = [0] * (n + 1)
        f[0] = 1

        for i in range(1, n+1):

            a = ord(str(s[i])) - ord('0')  # 『 位置 i 自己能否形成独立 item 』
            b = (ord(str(s[i - 1])) - ord('0')) * 10 + ord(str(s[i])) - ord('0')  # 『位置 i 能够与上一位置（i-1）能否形成 item』

            if 1 <= a <= 9:
                f[i] = f[i - 1]
            if 10 <= b <= 26:
                f[i] += f[i - 2]

        return f[n]


    def numDecodings_2(self, s):

        """
        f[i] 时只依赖 f[i-1] 和 f[i-2] 两个状态, 所以通过维护两个变量然后取消dp数组

        采用与「滚动数组」类似的思路，只创建长度为 3 的数组，通过取余的方式来复用不再需要的下标。

        """

        n = len(s)
        s = ' ' + s
        f = [0] * 3
        f[0] = 1
        for i in range(1, n + 1):
            f[i % 3] = 0
            a = ord(s[i]) - ord('0')
            b = (ord(s[i - 1]) - ord('0')) * 10 + ord(s[i]) - ord('0')
            if 1 <= a <= 9:
                f[i % 3] = f[(i - 1) % 3]
            if 10 <= b <= 26:
                f[i % 3] += f[(i - 2) % 3]
        return f[n % 3]

    def numDecodings_3(self, s):

        """

        dfs

        dfs(i): 从i位置开始到末尾的字符串有多少解码方案

        """

        def dfs(i):
            if i == len(s):
                return 1
            if i > len(s) or s[i] == "0":
                return 0
            if i < len(s) - 1 and int(s[i:i + 2]) <= 26:
                return dfs(i + 1) + dfs(i + 2)
            return dfs(i + 1)

        return dfs(0)


if __name__ == '__main__':

    s = Solution()
    s.numDecodings("226")
