def displayodd(str1):
    print("Characters at odd position are : ", str1[1::2])


def displayeven(str1):
    print("Characters at even position are : ", str1[::2])


def lenstr(str1):
    print("Length of a string is : ", len(str1))


def adda(str1):
    str1 = str1 + ("a" * len(str1))
    print("New string is : ", str1)
