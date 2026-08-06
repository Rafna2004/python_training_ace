s=input("enter the word:")
change=input("enter the re_word:")
new=input("enter the ch_word:")
words=s.split()
result=[]
for word in words:
    if word==change:
        result.append(new)
    else:
        result.append(word)
print(" ".join(result))