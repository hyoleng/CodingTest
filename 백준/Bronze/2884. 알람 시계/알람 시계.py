A, B = map(int, input().split())

if B < 45:
    B = B + 60 - 45
    if A == 0:
        A = 23
    else:
        A -= 1
else:
    B -= 45
    
print(A, B)

