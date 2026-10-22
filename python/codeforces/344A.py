n = int(input())
arr = []
s = 0
for i in range(n):
    arr.append(list(input()))
for j in range(n-1):
    if arr[j][1] != arr[j+1][0]:
        s += 1
print(n-s)
