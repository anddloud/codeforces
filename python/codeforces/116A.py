n_stops = input()
arr = []
for i in range(int(n_stops)):
    arr.append(input().split())
t = 0
max = 0
for i in range(int(n_stops)):
    for j in range(1):
        if int(t) > max:
            max = t
        t = t - int(arr[i][j])
        t = t + int(arr[i][j+1])
print(max)