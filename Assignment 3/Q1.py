def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Example usage:
n=int(input("Enter number"))
print(f"The digital root of {n} is {digital_root(n)}")