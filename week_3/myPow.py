

class Solution(object):

    def myPow(self, x, n):

        """
        分治法:

        pow(x, n)

        x为奇数: pow(x, n/2) * pow(x, n/2) * x

        x为偶数: pow(x, n/2) * pow(x, n/2)

        x 为负数: pow(x, n) = 1/ pow(x, -n)

        时间复杂度: O(logn)

        空间复杂度: O(1)


        """

        def sub_pow(N):
            if N == 0:
                return 1.0
            y = sub_pow(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return sub_pow(n) if n >= 0 else 1.0 / sub_pow(-n)
