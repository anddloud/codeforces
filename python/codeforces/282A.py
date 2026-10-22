t = int(input())
count = 0
for i in range(t):
    n = input()
    for j in range(3):
        if n[j] == "-":
            count = count - 1
            break
        elif n[j] == "+":
            count = count + 1
            break
print(count)