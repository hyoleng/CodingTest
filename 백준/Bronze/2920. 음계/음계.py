A = list(map(int, input().split()))
if A[0] == 1:
    for i in range(1, 8):
        if A[i] == i+1:
            pass
        else:
            print('mixed')
            exit()
    print('ascending')
elif A[0] == 8:
    for i in range(1, 8):
        if A[i] == A[0]-i:
            pass
        else:
            print('mixed')
            exit()
    print('descending')
else:
    print('mixed')