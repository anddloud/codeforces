num = input()
c = 0
for i in range(len(num)):
    if int(num[i]) == 4 or int(num[i]) == 7:
        c += 1
if c == 4 or c == 7:
    print("YES")
else:
    print("NO")