A = input()
B = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in B:
    A = A.replace(i, "*")
print(len(A))