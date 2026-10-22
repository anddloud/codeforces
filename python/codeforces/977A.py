arr = list(input().split())
sub = int(arr[1])
count = int(arr[0])
for i in range(sub):
    if int(str(count)[-1]) != 0:
        count -= 1
    else:
        count = count//10
print(count)
        


