n = int(input())
w = input()
c = 0
for i in range(n-1):
    if w[i] == w[i+1]:
        c += 1
print(c)