t = input()
num = len(t)
for j in range(len(t)-1):
    for i in range(j+1,len(t)):
        if t[i] == t[j]:
            num -= 1
            break
if num%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
        