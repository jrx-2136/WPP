L=[]
a=input("Enter Number of Students:")
for i in range(int(a)):
    b=input("Enter the name of student:")
    if len(b)>15:
        b=b[:15]
    L.append(b)
for name in L:
    print(name[::-1])


