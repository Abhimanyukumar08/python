def totalPrime(a,b):
    count = 0
    
    for i in range(a,b+1):
        if i==1:
            continue
        flag = True
        for j in range(2,i):
            if (i%j==0):
                flag = False
                break
        if flag:
            count +=1
    return count

S,E = map(int,input().split(' '))
print(totalPrime(S,E))

