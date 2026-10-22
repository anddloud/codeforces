n = list(input().split())
l = int(n[0])
b = int(n[1])
c = 0
while l<=b:
    l = l*3
    b = b*2
    c = c + 1
print(c)
