S = input()
X = 'abcdefghijklmnopqrstuvwxyz'

for i in X:
    if i in S:
        print(S.index(i), end = ' ')
    else:
        print(-1, end = ' ')