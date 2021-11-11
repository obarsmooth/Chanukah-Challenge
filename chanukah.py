def numofcandles(s):
    candles = s[0]
    days = s[1]
    
    candlesneeded = days + ((days * (days + 1))/2)
    print('{0} {1}'.format(candles,int(candlesneeded)))
    
n = int(input())
for i in range(n):
    s = [int(j) for j in input().split()]
    numofcandles(s)
