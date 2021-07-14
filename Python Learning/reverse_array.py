n = int(input())
arr = [int(x) for x in input().split()]
for i in range(n-1,-1,-1):
    print(arr[i],end=" ")