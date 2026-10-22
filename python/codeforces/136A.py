n = int(input())
arr = list(map(int,input().split()))
arr1 = []
mini = 0
c = -1
for i in range(n):
    mini = min(arr)
    for j in range(n):
        if arr[j] == mini:
            c = j
            arr1.append(c)
            arr[j] = float('inf')
for _ in range(len(arr1)):
    print(arr1[_]+1,end=" ")
        