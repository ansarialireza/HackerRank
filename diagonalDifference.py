# 1 2 3
# 4 5 6
# 9 8 9  

arr=[[1,2,3],[4,5,6],[9,8,9]]

def diagonalDifference(arr):
    left_to_right=0
    right_to_left=0
    for i in range(0,len(arr)):
        j=(len(arr)-1)-i
        left_to_right += arr[i][i]
        right_to_left += arr[i][j]

    return abs(left_to_right-right_to_left)
res=diagonalDifference(arr)
print(res)
            
# for i in range(7,0,-1):
#     print(i)