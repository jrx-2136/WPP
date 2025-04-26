def f(x,y):
    if x<=3: return x
    if y<4: return y
    return f(x-1,y-2)+f(x-3,y-4)
print(f(20,30))