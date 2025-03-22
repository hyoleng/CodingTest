X = []
for _ in range(9):
    A = list(map(int, input().split()))
    X.append(A)
a, b, c = 0, 0, 0
for i in range(9):
    for j in range(9):
        if X[i][j] > a:
            a = X[i][j]
            b = i
            c = j
print(X[b][c])
print(str(b+1), str(c+1))