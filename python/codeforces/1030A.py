num = int(input())
st = list(input().split())
b = True
for z in st:
    if z == '1':
        b = False
        break
if b == False:
    print('HARD')
    
else:
    print('EASY')

