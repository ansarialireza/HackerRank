def noonerize(numbers):
    if type(numbers[0])==int and type(numbers[1])==int:
        str1=str(numbers[0])
        str2=str(numbers[1])
        # print(str1,str2)
        temp1=str1[0]
        temp2=str2[0]
        str1=(str1.replace(str1[0],temp2))
        print(str1[0],str2[0])
        str2=int(str2.replace(str2[0],temp1))
        # print(str1,str2)

        # return abs(str1-str2)
    else:
        return 'invalid array'

# arr=[123, 456]
arr=[55, 63]
#65 53
# 66 53
# 53
#12
print(noonerize(arr))


# [123, 456] = 423 - 156 = 267



