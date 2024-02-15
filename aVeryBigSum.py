


def aVeryBigSum(ar):
    sum=0
    for i in ar:
        sum+=i
    return sum


arr=[1000000001 ,1000000002 ,1000000003 ,1000000004 ,1000000005]
res=aVeryBigSum(arr)
print(res)