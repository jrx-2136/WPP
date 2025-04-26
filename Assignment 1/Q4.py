list = [[],[],[],[],[]]

for i in range (1,10001):
    list[i%5].append(i)
  
print("Equivalence class of 5:")
for i in range (0,5):
    print("List of numbers with remainder",i)
    print(list[i][:50])