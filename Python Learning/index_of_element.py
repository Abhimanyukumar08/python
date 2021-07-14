n = int(input())
array = [int(x) for x in input().split()]
target = int(input())
def first_index(array,length,target):

    for i in array:
        if i == target:
            return array.index(i)
    return -1   
print(first_index(array,n,target))