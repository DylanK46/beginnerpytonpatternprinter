def printpattern(number): 
    for i in range(0, number): 
        for j in range(0, i+1): 
            print("* ",end="") 
        print("\r") 

print("Input Number of rows ")
print("/n")
printpattern(int(input()))
