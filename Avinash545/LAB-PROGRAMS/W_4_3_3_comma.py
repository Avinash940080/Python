def comm(x):
    return x.replace('', ',')[1:-1]


x = "Hello,World,,,"
print(repr(comm(x)))