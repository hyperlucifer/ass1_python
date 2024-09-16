# write a python program to count repited characters in a string

s="thequickbrownfoxjumpsoverethelazydog"

c={}
for i in s:
    if i in c:
        c[i]+=1
    else:
        c[i]=1

print(c)