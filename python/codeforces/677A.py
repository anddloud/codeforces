num = list(map(int,input().split()))
num1 = list(map(int,input().split()))
c = 0
for i in range(num[0]):
    if num1[i] > num[1]:
        c += 2
    else:
        c += 1
print(c)