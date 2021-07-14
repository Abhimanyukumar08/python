n = int(input())
arr = [int(x) for x in input().split()]
rotate = int(input())
for i in range(rotate):
    temp = arr[0]
    for j in range(n-1):
        arr[j] = arr[j+1]
       
    arr[n-1]=temp
print(*arr)
