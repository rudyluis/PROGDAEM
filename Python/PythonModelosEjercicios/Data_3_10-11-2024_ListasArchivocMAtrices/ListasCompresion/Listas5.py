a=[1,5,3,6,8,10]
b=[0,0,0,0,0,0]
print(a)
for _ in range(len(a)):
    if(a[_] % 2==0):
        ###b[i]=a[i]
        b[_]=a[_]

print(b)

##b=[0,0,0,6,8,10]