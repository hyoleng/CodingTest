N, M = map(int, input().split())
ball = [0 for i in range(N)]
for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i-1, j):
        ball[x] = k
for i in ball:
    print(i, end = " ")