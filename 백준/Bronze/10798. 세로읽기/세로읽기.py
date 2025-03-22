X = []
Y = []
for _ in range(5):
    A = input()
    X.append(A)
    Y.append(len(A))

n = ''
for i in range(max(Y)):
    for j in range(5):
        if i < Y[j]:
            n += X[j][i]

print(n)