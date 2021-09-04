
"""

https://leetcode-cn.com/problems/search-a-2d-matrix/

搜索二维矩阵

"""


class Solution(object):

    def searchMatrix(self, matrix, target):

        """

        解法一: 二分查找

        按行遍历二维矩阵本质上是一个升序数组

        时间复杂度: O(logmn), mn可以理解为一个一维数组的长度

        空间复杂度: O(1)

        """

        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) >> 1
            x, y = mid // n, mid % n
            if matrix[x][y] > target:
                r = mid - 1
            elif matrix[x][y] < target:
                l = mid + 1
            else:
                return True
        return False

    def searchMatrix_2(self, matrix, target):

        """

        时间复杂度: O(m+n)

        空间复杂度: O(1)
        """

        rows = len(matrix) - 1
        cols = len(matrix[0])
        columns = 0

        while rows >= 0 and columns < cols:
            num = matrix[rows][columns]
            if num == target:
                return True
            elif num > target:
                rows -= 1
            else:
                columns += 1

        return False
