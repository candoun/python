# coding=utf-8
"""
1, 将数组1和数组2各列分别求和
2， 将一串字符串的每个单词首字母更改为大写，其他为小写
"""

list1 = [1, 2, 3]
list2 = [4, 5, 6]
s = "hello tHis worLD!"



def summing(a, b):
    return a+b


def map_list(list1, list2):
    return map(summing, list1, list2)


# 首字母大写转化
def upper_first(slist):
    slist_upper = slist[0:1].upper()+slist[1:].lower()
    return slist_upper


def map_upper(s):
    slist = s.split(' ')
    slist_u = map(upper_first, slist)
    result = ' '.join(slist_u)
    return result


if __name__ == "__main__":
    print(map_list(list1, list2))
    print(map_upper(s))

