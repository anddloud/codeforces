n = list(input().split("+"))
n = sorted(n)
count = 0
for i in range(len(n)):
    print(n[i],end="")
    if count != len(n)-1:
        print("+",end="")
        count = count + 1

