
"""

有效的完全平方数
https://leetcode-cn.com/problems/valid-perfect-square/


"""


class Solution(object):

    def isPerfectSquare(self, num):


        """

        二分查找求平方根

        """

        if num < 2:
            return True

        l = 1
        r = num // 2

        while l <= r:

            mid = l + (r - l) // 2

            guess_squared = mid * mid

            if guess_squared > num:
                r = mid - 1
            elif guess_squared < num:
                l = mid + 1
            else:
                return True

        return False

    def isPerfectSquare_2(self, num):

        """

        二分查找求平方根

        """

        r = num
        while r * r > num:
            r = (r + num / r) // 2
        return r * r == num


if __name__ == '__main__':

    s = Solution()
    res = s.isPerfectSquare(14)
    print(res)





