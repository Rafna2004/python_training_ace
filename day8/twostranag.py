def isAnagram(s, t):
    return sorted(s) == sorted(t)


s = input("Enter first string: ")
t = input("Enter second string: ")


if isAnagram(s, t):
    print("Anagram")
else:
    print("Not Anagram")


"""
x=input("enter the first string: ")
y=input("enter the second string: ")
if sorted(x.lower())==sorted(y.lower()):
print("Anagram")
else:
print("Not Anagram")

"""