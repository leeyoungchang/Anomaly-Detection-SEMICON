

def myfunction(num):
    
    N = len(str(num))
    sum = 0
    for n in range(N):
     
        print(str(num)[n])
        sum += int(str(num)[n])

    return num + sum

print(myfunction(123))