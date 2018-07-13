#coding=utf-8
"""
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个16位激活码（或者优惠券）？
"""
import random


list1 = []
m = 16
n = 20
promtions = []


def create_promotion(m):
    s = ''
    for x in range(65, 91):
        a = str(chr(x))
        list1.append(a)
    for x in range(97, 123):
        b = str(chr(x))
        list1.append(b)
    for x in range(10):
        c = str(x)
        list1.append(c)
    for x in range(m):
        a = random.choice(list1)
        s += a
    return s


def create_promotions(num):
    for i in range(num):
        promtion = create_promotion(m)
        promtions.append(promtion)
    return promtions


if __name__ == "__main__":
    a = create_promotions(n)
    for x in a:
        print(x)
