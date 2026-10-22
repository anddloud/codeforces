n = int(input())
count1 = 0
for i in range(n):
    num = str(input())
    count = 0
    for j in range(0,5,2):
        if int(num[j]) == 1:
            count = count + 1
    if count >= 2:
        count1 = count1 + 1
print(count1)