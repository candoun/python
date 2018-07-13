# coding=utf-8
"""
将test.txt文本中每行的首字母大写，其余字母小写
"""

def file2list(filename):
    datalist = []
    with open(filename, 'r') as f:
        for line in f:
            datalist.append(line)
    return datalist


def upper_word(s):
    return s[0:1].upper()+s[1:].lower()


def capitalized(filename):
    datalist = file2list(filename)
    upper_list = map(upper_word, datalist)
    return ''.join(upper_list)


def write2file(filename, s):
    with open(filename, 'w') as f:
        f.write(s)


if __name__ == "__main__":
    s = capitalized("test.txt")
    write2file("test_new.txt", s)
