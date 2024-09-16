# write a python script to generate and print a dictionary which contains a number 
# (between 1 and n ) in the form of (x,x*x) 

n=int(input("enter the n^th number "))

d={}
print(type(d))

for i in range (1,n+1):
    d[i]=i*i

print(d)