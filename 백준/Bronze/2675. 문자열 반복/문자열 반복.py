T = int(input())
for _ in range(T):
    X = input().split()
    R = int(X[0])
    S = X[1]
    for i in S:
        print(i * R, end = '')
    print()