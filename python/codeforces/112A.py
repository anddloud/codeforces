t1 = input().lower()
t2 = input().lower()
con = True
loc = -1
for i in range(len(t1)):
    if ord(t1[i]) != ord(t2[i]):
        con = False
        loc = i
        break
if con == True:
    print(0)
else:
    if ord(t1[loc]) < ord(t2[loc]):
        print(-1)
    else:
        print(1)
    
        