A = input().upper()
B = list(set(A))
X = []
for i in B:
    X.append(A.count(i))
if X.count(max(X)) >= 2:
    print("?")
else:
    print(B[X.index(max(X))])