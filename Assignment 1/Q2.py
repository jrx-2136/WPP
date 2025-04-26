import random
L=[]
for i in range(1,100):
    L.append(random.randint(0,1))
print(L)

long = 0
current = 0

for num in L:
    if num == 0:
        current += 1
        if current > long:
            long = current
    else:
        current = 0

print("The longest run of zeros is:", long)