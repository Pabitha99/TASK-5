rows = 20  
#pyramid of numbers from 1 to 20 
for i in range(1, rows + 1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()  