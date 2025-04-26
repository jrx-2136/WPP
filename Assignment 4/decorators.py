def func_deco_1(func):
    def wrapper(x):
        print("Initial value in 1 is",x)
        x+=50
        print("Changed value in 1 passed to func",x)
        return func(x)
    return wrapper

def func_deco_2(func):
    def wrapper(x):
        print("Initial value in 2",x)
        x-=20
        print("Changed value in 2 passed to func",x)
        return func(x)
    return wrapper
@func_deco_1
@func_deco_2
def func(x):
    print("Initial value in func",x)
    print("Changed value in func",x+10)
    return x+10
print(func(50))