
a=[5,6,7,8]
b=[3,6,10]


def compareTriplets(a, b):
    alice=0
    bob=0
    for i in range(len(a)):
        if a[i]>b[i]:
            alice=alice+1
        elif a[i]<b[i]:
            bob=bob+1
    return(alice,bob)

result = compareTriplets(a, b)
print(result)