

"""

https://leetcode-cn.com/problems/majority-element/

多数元素


"""


class Solution(object):

    def majorityElement(self, nums):

        """

        摩尔投票法


        """

        candidate = None
        count = 0

        for v in nums:
            if count == 0:
                candidate = v

            if v == candidate:
                count += 1
            else:
                count -= 1
        return candidate
