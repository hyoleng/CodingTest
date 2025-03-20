A = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0}
cnt = 0
sum = 0
for _ in range(20):
    X = list(input().split())
    if X[2] == 'P':
        continue
    else:
        cnt += float(X[1])
        sum += float(X[1]) * float(A[X[2]])
print(sum / cnt)