N, M = map(int, input().split())
A = []
B = []
for _ in range(N):
    Z = list(map(int, input().split()))
    A.append(Z)
for _ in range(N):
    Z = list(map(int, input().split()))
    B.append(Z)
for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end = ' ')
    print()