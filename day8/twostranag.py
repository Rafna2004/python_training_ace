def isAnagram(s, t):
    return sorted(s) == sorted(t)


s = input("Enter first string: ")
t = input("Enter second string: ")


if isAnagram(s, t):
    print("Anagram")
else:
    print("Not Anagram")