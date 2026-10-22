w1 = input()
w2 = input()
b = True
for i in range(len(w1)):
    if len(w1) == len(w2) and w1[i] != w2[abs(i-len(w1)+1)]:
        b = False
if len(w1) != len(w2):
    b = False
if b:
    print('YES')
else:
    print('NO')