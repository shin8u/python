n = int(input())
a = []
snowman = []
for i in range(0, n):
    x = int(input())
    a.append(x)
a.sort()
snowman.append(a[0])
i = 1
f = 0
while i < n:
    if a[i] != a[i-1]:
        if len(snowman) < 3:
            snowman.append(a[i])
        if len(snowman) == 3:
            print(snowman)
            snowman.clear()
            i -= 1
            f += 1
    i += 1
print(f)
