sq = list(map(int,input().split()))
if sq[0]%2 != 0 and sq[1]%2 != 0:
    print(int((sq[0]*sq[1]-1)/2))
else:
    print(int(sq[0]*sq[1]/2))