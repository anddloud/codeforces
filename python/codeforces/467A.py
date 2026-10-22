num = int(input())
arr = []
c = 0
for i in range(num):
    arr.append(list(map(int,input().split())))
for i in range(num):
    if arr[i][0]+2 > arr[i][1]:
        continue
    else:
        c += 1
print(c)