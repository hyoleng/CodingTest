N = int(input())
M = list(map(int, input().split()))
X = []
for i in M:
    X.append(i/max(M)*100)
print(sum(X)/N)