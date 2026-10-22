from math import isclose
n = int(input())
s = 0
arr = list(map(int,input().split())) 
for num in arr:
    s += num
    
print(f'{s/n:.12f}')
