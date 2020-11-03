https://www.hackerrank.com/challenges/birthday-cake-candles/problem

solution 

def birthdayCakeCandles(candles):
    m=candles[0]
    for i in range(len(candles)):
        if(candles[i]>m):
            m=candles[i]
    c=candles.count(m)
    return c

