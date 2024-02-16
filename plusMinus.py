



def plusMinus(arr):

    def precision_print(input):
        print("{0:.6f}".format(input))

    positive_counter=0
    negative_counter=0
    zero_counter=0
    arr_len=len(arr)

    for i in arr:
        if i>0:
            positive_counter+=1
        elif i==0:
            zero_counter+=1
        else:
            negative_counter+=1

    positive=positive_counter/arr_len
    negative=negative_counter/arr_len
    zero=zero_counter/arr_len
    
    precision_print(positive)
    precision_print(negative)
    precision_print(zero)
            

arr=[1,1,0,-1,-1]

plusMinus(arr)