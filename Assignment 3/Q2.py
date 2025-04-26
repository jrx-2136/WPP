L=[]
def fibo(n):
    if n <= 1:
        L.append(n)
    else:
        a=fibo(n - 1) + fibo(n - 2)
        L.append(a)
n = int(input("Enter the number of terms: "))
fibo(n)
given=int(input("Enter number to check:"))
if given in L:
    print("IsFibo")
else:
    print("IsNotFibo")