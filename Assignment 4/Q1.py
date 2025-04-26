def numberofchangesmade(input_word):
    total_operations=0
    length = len(input_word)
    for index in range(length//2):
        l_letter=ord(input_word[index])
        r_letter=ord(input_word[length-index-1])
        total_operations += abs(l_letter - r_letter) 
    return total_operations

test_cases = int(input("Enter number of test cases:"))
for _ in range(test_cases):
    input_word = input("Enter string:").strip()
    result = numberofchangesmade(input_word)
    print(result)