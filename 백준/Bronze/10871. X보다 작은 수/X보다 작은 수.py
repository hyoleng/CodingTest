N, X = map(int, input().split())
M = list(map(int, input().split()))
for i in M:
    if X > i:
        print(i, end = " ")