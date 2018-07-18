# coding = utf-8


def foo(a):
    print(a)


def foo1(*args):
    print(args)


def foo2(**kwargs):
    print(kwargs)


if __name__ == "__main__":
    foo1("good", "good", "study")
    foo2(a1="day", a2="day", a3="up")
    aa = {"depoy_process": "deploying"}
    foo2(**aa)
