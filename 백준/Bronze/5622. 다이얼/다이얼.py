dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
X = input()
result = 0
for i in X:
    for j in dial:
        if i in str(j):
            n = dial.index(j) + 3
            result += n
print(result)