
def miniMaxSum(arr):
    arr.sort()
    min=0
    max=0
    for i in range(0,4):
        min+=arr[i]
    for i in range(4,0,-1):
        max+=arr[i]
    print(min,max)
    # Write your code here



# arr=[1,3,5,7,9]
arr=[3,1,9,5,7]
miniMaxSum(arr)