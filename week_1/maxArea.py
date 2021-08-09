
"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。

在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
"""

"""
思路一：枚举


思路二: 左右夹逼法则



思路三:


"""


class MaxArea(object):

    def solution_1(self, height):
        """
        :type height: List[int]
        :rtype: int

        暴力循环, 枚举所有的值
        """

        max_area = 0
        for i in range(0, len(height) - 1):  # i 不能指向最后一个元素, 否则会导致j index out of  range
            for j in range(i+1, len(height)):
                area = (j - i) * min(height[i], height[j])
                max_area = max(area, max_area)
        return max_area

    def solution_2(self, height):

        """
        :param height:
        :return:
        """

        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            if height[i] < height[j]:
                min_height = height[i]
                i += 1
            else:
                min_height = height[j]
                j -= 1

            max_area = max(max_area, (j - i + 1) * min_height)  # 因为 i 或者 j 已经移动，所以宽度需要 (j - i) + 1

        return max_area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    ma = MaxArea()
    ma.solution_2(height)


