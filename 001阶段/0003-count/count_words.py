# coding=utf-8
"""
1，统计test.txt文本每个单词出现的次数
2，打印出现频率最高的五个单词
"""
from collections import Counter
import re


def create_list(file_name):
    datalist = []
    with open(file_name) as f:
        for line in f:
            content = re.sub("\"|,|\.", "", line)
            datalist.extend(content.strip().split(' '))
    return datalist


def wc(file_name):
    datalist = create_list(file_name)
    return Counter(datalist)


if __name__ == "__main__":
    file_name = "test.txt"
    result = (wc(file_name))
    print(result)
    print(result.most_common(5))
