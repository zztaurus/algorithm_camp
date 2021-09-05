
"""

https://leetcode-cn.com/problems/fizz-buzz/

"""

class FizzBuzz(object):

    def solution_1(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ans = list()
        for i in range(n):
            mod_3 = (i+1) % 3
            mod_5 = (i+1) % 3
            if mod_3 == 0 and mod_5 == 0:
                ans.append("FizzBuzz")
            elif mod_3 == 0:
                ans.append("Fizz")
            elif mod_5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i+1))

        return ans

