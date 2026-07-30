def anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        str1 = sorted(str1)
        str2 = sorted(str2)
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False
            else:
                return True

str1 = "anagram"
str2 = "nagaram"
print(anagram(str1, str2))

    