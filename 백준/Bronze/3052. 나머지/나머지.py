num = []
for i in range(10):
    x = int(input())
    num.append(x % 42)
num = set(num)
print(len(num))