def bigger_is_greater(w):
    w = list(w)
    n = len(w)
    pivot = -1
    
    # Step 1: Find the pivot
    for i in range(n - 2, -1, -1):
        if w[i] < w[i + 1]:
            pivot = i
            break
    
    if pivot == -1:
        return "no answer"
    
    # Step 2: Find the swap candidate
    for i in range(n - 1, pivot, -1):
        if w[i] > w[pivot]:
            break
    
    # Step 3: Swap the pivot and swap candidate
    w[pivot], w[i] = w[i], w[pivot]
    
    # Step 4: Sort the substring to the right of the pivot
    w[pivot + 1:] = sorted(w[pivot + 1:])
    
    return ''.join(w)

# Read the number of test cases
t = int(input("Enter the number : "))
for _ in range(t):
    w = input().strip()
    result = bigger_is_greater(w)
    print(result)