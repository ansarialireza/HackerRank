

def birthdayCakeCandles(candles):
    candles.sort()
    res=candles[-1:]
    counter=0
    for i in range(0,len(candles)):
        if candles[i]==res[0]:
            counter+=1
    return counter


input=[3,2,1,3]
result=birthdayCakeCandles(input)
print(result)
