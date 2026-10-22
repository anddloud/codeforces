num = int(input())
w = input()
ca = 0
cd = 0
for i in range(num):
    if w[i] == 'A':
        ca += 1
    else:
        cd += 1
if ca > cd:
    print('Anton')
elif cd > ca:
    print('Danik')
else:
    print('Friendship')