
"""

两个数组的交集 II

"""


class Intersect(object):

    def solution_1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        由于同一个数字在两个数组中都可能出现多次，因此需要用哈希表存储每个数字出现的次数。对于一个数字，其在交集中出现的次数等于该数字在两个数组中出现次数的最小值。

        首先遍历第一个数组，并在哈希表中记录第一个数组中的每个数字以及对应出现的次数，然后遍历第二个数组，对于第二个数组中的每个数字，如果在哈希表中存在这个数字，则将该数字添加到答案，并减少哈希表中该数字出现的次数。

        为了降低空间复杂度，首先遍历较短的数组并在哈希表中记录每个数字以及对应出现的次数，然后遍历较长的数组得到交集。

        """

        if len(nums2) < len(nums1):
            return self.solution_1(nums2, nums1)
        num_count_dict = dict()
        res = []
        for i in nums1:
            if i not in num_count_dict:
                num_count_dict.update({i : 1})
            else:
                num_count_dict[i] += 1

        for j in nums2:
            if j in num_count_dict and num_count_dict[j] > 0:
                res.append(j)
                num_count_dict[j] -= 1

        return res


    def solution_2(self, nums1, nums2):

        nums1.sort()
        nums2.sort()
        intersect = list()
        len1, len2 = len(nums1), len(nums2)
        index1 = index2 = 0
        while index1 < len1 and index2 < len2:

            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                intersect.append(nums1[index1])
                index1 += 1
                index2 += 1

        return intersect








