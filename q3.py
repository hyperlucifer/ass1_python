# write a python code to compute a element wise sum of 3 tuples

t1=(1,2,3)
t2=(4,5,6)
t3=(7,8,9)

t4=[]
for i in range(3):
    t4.append(t1[i]+t2[i]+t3[i])

t4=tuple(t4)
print(t4)