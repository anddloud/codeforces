n = input()
pl = list(map(int,n.split(' ')))
t = pl[0]
place = pl[1]
count = 0
l = input()
list1 = list(map(int,l.split(' ')))
for i in range(t):
    if list1[i] >= list1[place-1] and list1[i] != 0:
        count = count + 1
print(count)