
"""
有效的字母异位词

https://leetcode.com/problems/valid-anagram/description/

"""


class Solution(object):


    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        result = True

        if set(s) == set(s):
            for i in s:
                result = result and (s.count(i) == t.count(i))

        else:
            return False

        return result



