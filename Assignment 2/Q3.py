test_cases = int(input("Enter the number of test cases: "))
numbers = []

for _ in range(test_cases):
    num = int(input("Enter the number: "))
    numbers.append(num)

for num in numbers:
    temp = num
    count = 0

    while num > 0:
        digit = num % 10
        num //= 10
        if digit != 0 and temp % digit == 0:
            count += 1

    print(count)

