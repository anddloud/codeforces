y = input()
x = int(y)+1
y = set(str(x))
while True:
    if len(y) == 4:
        print(x)
        break
    else:  
        x += 1
        y = set(str(x))
        
    