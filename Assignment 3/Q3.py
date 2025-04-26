def utopian_tree_height(cycles):
    height = 1
    for cycle in range(1, cycles + 1):
        if cycle % 2 == 1:  
            height *= 2
        else:  
            height += 1
    return height

def main():
    T = int(input("Enter the number of test cases: "))
    results = []
    for i in range(T):
        N = int(input("Enter the number of cycles: "))
        results.append(utopian_tree_height(N))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()