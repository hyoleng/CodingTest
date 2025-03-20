A = list(input())
for i in range(len(A)):
    if A[i].islower() == True:
        A[i] = A[i].upper()
    elif A[i].isupper() == True:
        A[i] = A[i].lower()
print(*A, sep = '')