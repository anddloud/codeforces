arr = list(map(int,input().split()))
q = list(input())
for i in range(arr[1]):
    c = 1
    while c < arr[0]:
        if q[c-1] == 'B' and q[c] == 'G':
            q[c-1] , q[c] = q[c], q[c-1]
            c += 1
        c += 1    
            
        
for words in q:
    print(words,end='')