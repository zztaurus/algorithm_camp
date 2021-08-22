
"""

https://leetcode-cn.com/problems/get-kth-magic-number-lcci/


面试题 17.09. 第 k 个数

"""

import heapq


class Solution(object):

    def getKthMagicNumber(self, k):
        """

        三指针法, 如何理解三指针：

        一个丑数总是由前面的某一个丑数 x3 / x5 / x7 得到。反过来说也是一样的，一个丑数 x3 / x5 / x7 就会得到某一个更大的丑数。

        如果把丑数数列叫做 ugly[i]，那么考虑一下三个数列：
        1. ugly[0]*3,ugly[1]*3,ugly[2]*3,ugly[3]*3,ugly[4]*3,ugly[5]*3……
        2. ugly[0]*5,ugly[1]*5,ugly[2]*5,ugly[3]*5,ugly[4]*5,ugly[5]*5……
        3. ugly[0]*7,ugly[1]*7,ugly[2]*7,ugly[3]*7,ugly[4]*7,ugly[5]*7……

        上面这个三个数列合在一起就形成了新的、更长的丑数数列。

        如果合在一起呢？这其实就是一个合并有序线性表的问题。

        定义三个index 分别指向上面三个数列，下一个丑数一定是三个 index 代表的值中最小的那个。然后相应 index++ 即可。


        """

        nums, p3, p5, p7 = [1] * k, 0, 0, 0
        for i in range(1, k):
            nums[i] = min(nums[p3] * 3, nums[p5] * 5, nums[p7] * 7)
            print(nums[p3] * 3, nums[p5] * 5, nums[p7] * 7)
            print(i, nums[i])
            if nums[i] == nums[p3] * 3: p3 += 1
            if nums[i] == nums[p5] * 5: p5 += 1
            if nums[i] == nums[p7] * 7: p7 += 1
        print(nums)
        return nums[k - 1]


    def getKthMagicNumber_2(self, k):
        """

        小顶堆

        每次都从堆中取出最小的元素，然后依次 乘以 3，5，7 放入堆中。
        """

        heap = [1]
        for i in range(k):
            print(heap)
            res = heapq.heappop(heap)
            while heap and res == heap[0]:  # 去除重复元素
                heapq.heappop(heap)
            heapq.heappush(heap, res * 3)
            heapq.heappush(heap, res * 5)
            heapq.heappush(heap, res * 7)

        return res


if __name__ == '__main__':
    s = Solution()
    res = s.getKthMagicNumber(30)
    print(res)

