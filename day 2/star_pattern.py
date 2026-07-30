def starPattern(num):
    for i in range(num):
        for j in range(i + 1):
            print("*", end="")
        print() 

num = int(input("Enter: "))
starPattern(num)


def starPattern(num):
    for i in range(1,num+1):
        print(" "*(num-i),"*"*i)

num = int(input("Enter: "))
starPattern(num)