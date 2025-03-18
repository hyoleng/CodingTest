N, M = map(int, input().split())
X = [i+1 for i in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    temp = X[i-1:j]
    temp.reverse()
    X[i-1:j] = temp
print(*X)