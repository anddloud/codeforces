arr = list(map(int,input().split()))
d_b = arr[0]
d = arr[1]
target = arr[2]
c = 0
for i in range(1,target+1):
    if d >= i*d_b:
        d = d - i*d_b
    else:
        c = c + abs(d - i*d_b)
        d = 0
print(c)