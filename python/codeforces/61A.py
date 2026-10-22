b1 = input()
b2 = input()
res = []
for i in range(len(b1)-1,-1,-1):
    add = 0
    add = int(b1[i]) + int(b2[i])
    if add == 2:
        res.append(0)
    elif add == 1:
        res.append(1)
    else:
        res.append(0)
for _ in range(len(res)-1,-1,-1):
    print(res[_],end="")
        