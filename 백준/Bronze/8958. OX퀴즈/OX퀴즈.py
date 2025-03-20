T = int(input())
for _ in range(T):
    A = input()
    score = 0
    cnt = 0
    if A[0] == 'O':
        score += 1
        cnt += 1
    for i in range(1, len(A)):
        if A[i] == 'O':
            if A[i-1] == 'O':
                cnt += 1
                score += cnt
            else:
                score += 1
                cnt = 1
        else:
            cnt = 1
            continue
    print(score)