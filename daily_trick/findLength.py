
"""

https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/

最长重复子数组

"""


class Solution(object):

    def findLength_1(self,  nums1, nums2):

        """

        暴力法

        时间复杂度 最坏时间复杂度为 O(n^3)
        空间复杂度 O(1)

        """

        ans = 0
        for i in range(len(nums1) - 1):
            for j in range(len(nums2) - 1):
                k = 0
                while nums1[i+k] == nums2[j+k]:
                    k += 1
                ans = max(ans, k)

        return ans

    def findLength_2(self, nums1, nums2):

        """
        动态规划

        如果 A[i] == B[j]，那么我们知道 A[i:] 与 B[j:] 的最长公共前缀为 A[i + 1:] 与 B[j + 1:] 的最长公共前缀的长度加一，否则我们知道 A[i:] 与 B[j:] 的最长公共前缀为零。

        状态:

            如果 A[i] == B[j]，那么我们知道 A[i:] 与 B[j:] 的最长公共前缀为 A[i + 1:] 与 B[j + 1:] 的最长公共前缀的长度加一，否则我们知道 A[i:] 与 B[j:] 的最长公共前缀为零


        转移方程:


            dp[i][j] = 0                    nums1[i] != nums[j]

            dp[i][j] = 1 + dp[i+1][j+1]     nums1[i] == nums[j]


        时间复杂度: O(mn)

        空间复杂度: O(mn)

        """

        n, m = len(nums1), len(nums2)

        dp = [[0] * (m + 1) for _ in range(0, n + 1)]
        ans = 0

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                ans = max(ans, dp[i][j])
        return ans

    def findLenght_3(self, nums1, nums2):

        """

        滑动窗口

        时间复杂度: O((N+M)×min(N,M))。

        空间复杂度: O(1)。


        """

        def maxLength(addA, addB, length):
            ret = k = 0
            for i in range(length):
                if nums1[addA + i] == nums2[addB + i]:
                    k += 1
                    ret = max(ret, k)
                else:
                    k = 0
            return ret

        n, m = len(nums1), len(nums2)
        ret = 0
        for i in range(n):
            length = min(m, n - i)  # nums2首部与nums1第i个位置对齐
            ret = max(ret, maxLength(i, 0, length))
        for i in range(m):
            length = min(n, m - i)  # nums1首部与nums2第i个位置对齐
            ret = max(ret, maxLength(0, i, length))
        return ret

