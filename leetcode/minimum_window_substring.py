
"""
Leet code 76: 最小覆盖子串

给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

    注意：

    对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
    如果 s 中存在这样的子串，我们保证它是唯一的答案。


    示例 1：

    输入：s = "ADOBECODEBANC", t = "ABC"
    输出："BANC"
    解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
    示例 2：

    输入：s = "a", t = "a"
    输出："a"
    解释：整个字符串 s 是最小覆盖子串。
    示例 3:

    输入: s = "a", t = "aa"
    输出: ""
    解释: t 中两个字符 'a' 均应包含在 s 的子串中，
    因此没有符合条件的子字符串，返回空字符串。

"""

def sub_string(s, t):
    l = 0
    r = 0
    len_s = len(s)
    min_sub_str = ""
    map_source = {}
    map_des = {}
    for sub_s in t:
        if sub_s not in map_source:
            map_source[sub_s] = 1
        else:
            map_source[sub_s] += 1
    while(r < len_s):
        r_char = s[r]
        r += 1
        if r_char not in map_des:
            map_des[r_char] = 1
        else:
            map_des[r_char] += 1
        while(check(map_source, map_des)): # 得到一个可行的子串, 开始收缩以便得到最小子串  l < r 这个条件不需要，因为当 l = r 时check 条件会先成立
            # 收缩窗口
            l_char = s[l]
            sub_str = s[l:r]
            if not min_sub_str or len(sub_str) < len(min_sub_str):
                min_sub_str = sub_str
            if l_char in map_des and map_des[l_char] > 0:
                    map_des[l_char] -= 1
            l += 1
    return min_sub_str



def check(m1, m2):
    for key, value in m1.items():
        if key in m2 and m2[key] >= value:
            continue
        else:
            return False
    return True


#  事件复杂度:
#  空间复杂度:

if __name__ == '__main__':
    print(sub_string("EBBANCF", "E"))



