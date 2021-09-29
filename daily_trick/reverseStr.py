
"""

https://leetcode-cn.com/problems/reverse-string-ii/

反转字符串 II

"""


class Solution(object):

    def reverseStr(self, s, k):


        """
        反转每个下标从 2k 的倍数开始的，长度为 k 的子串。若该子串长度不足 k，则反转整个子串。

        """

        t = list(s)
        for i in range(0, len(t), 2 * k):
            t[i: i + k] = reversed(t[i: i + k])
        return "".join(t)



