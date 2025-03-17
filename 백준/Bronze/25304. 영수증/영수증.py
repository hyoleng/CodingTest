N = int(input())
M = int(input())
X = 0
for i in range(M):
    A, B = map(int, input().split())
    X += (A * B)
if N == X:
    print("Yes")
else:
    print("No")