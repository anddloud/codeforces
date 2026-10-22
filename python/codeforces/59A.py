words = input()
c_lower = 0
c_upper = 0
for word in words:
    if ord(word) > 94:
        c_lower += 1
    else:
        c_upper += 1
if c_lower >= c_upper:
    print(words.lower())
else:
    print(words.upper())