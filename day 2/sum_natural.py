def sumNatural(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total

num = int(input("Enter num: "))
print("Sum:", sumNatural(num))