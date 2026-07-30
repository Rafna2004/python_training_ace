def reverse(x):
    if x >= 2 ** 31 - 1 or x <= -2 ** 31:
        return 0
    else:
        if x < 0:
            x = str(x)[1:]
            x = int(x[::-1])
            return -x
        else:
            x = str(x)
            x = int(x[::-1])
            return x

x =123
print(reverse(x))
x = -123
print(reverse(x))
x = 120
print(reverse(x))