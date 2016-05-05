# Add a comment line.
def mySort(cmp, *args):
    ret = []
    for arg in args:
        for idx, value in enumerate(ret):
            if cmp(arg, value):
                ret.insert(idx, arg)
                break
        else:
            ret.append(arg)
    return ret


# Define a compare function.
def cmp1(x, y):
    return x >= y


def cmp2(x, y):
    return x <= y


print("Using cmp1")
print(mySort(cmp1, 1, 3, 7, 2, 9, 4, 6, 8))
print("Using cmp2")
print(mySort(cmp2, 1, 3, 7, 2, 9, 4, 6, 8))
