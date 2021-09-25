
"""

https://leetcode-cn.com/problems/relative-sort-array/

数组的相对排序

"""


class Solution(object):

    def relativeSortArray(self, arr1, arr2):

        """
        计数排序：

        时间复杂度：O(m + n)，其中 m 和 n 分别为数组的长度，需要遍历一遍两个数组。

        空间复杂度：O(1)，额外开辟常数级别的存储空间。

        """

        arr = [0 for _ in range(1001)]
        ans = []
        for i in range(len(arr1)):
            arr[arr1[i]] += 1

        # 处理出现在arr2中的元素
        for i in range(len(arr2)):
            while arr[arr2[i]] > 0:
                ans.append(arr2[i])
                arr[arr2[i]] -= 1

        # 处理未出现在arr2中的元素
        for i in range(len(arr)):  # 使用arr数组，将arr2中出现过的元素需要按照升序放在arr1的末尾
            while arr[i] > 0:
                ans.append(i)
                arr[i] -= 1
        return ans

