n = list(input())
if ord(n[0]) > 90:
    n[0] = chr(ord(n[0])-32)
for i in range(len(n)):
    print(n[i],end="")