n = int(input())
array = [int(x) for x in input().split()]
target = int(input())
def first_index(array,length,target):

    for i in range(length-1, -1, -1):
        if array[i]==target:
            return i
        
    return -1   
print(first_index(array,n,target))
