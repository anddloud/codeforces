matrix = []
t = 0
for i in range(5):
    matrix.append(list(map(int,input().split())))
locat = []
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            locat.append(i)
            locat.append(j)
            break
while locat[0] !=2 or locat[1] !=2:
    if locat[0] != 2:
        if locat[0] > 2:
            locat[0] -= 1
        else:
            locat[0] += 1
        t += 1
    if locat[1] != 2:
        if locat[1] > 2:
            locat[1] -= 1
        else:
            locat[1] += 1
        t += 1
print(t)   
    
'''
matrix = []
for i in range(5):
    matrix.append(list(map(int,input().split())))

moves = 0
for row in matrix :
    if 1 in row :
        moves += abs(2-matrix.index(row)) + abs(2-row.index(1))
        break
print(moves)
'''