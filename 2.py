n = int(input())
a = []
snowman = []
for i in range(0, n):
    x = int(input())
    a.append(x)
a.sort()
print(n)
print(a)
f = 0
l = n // 3
for j in range(0, l):
    i = 0
    while i < n:
        if len(snowman) == 0:
            if a[i] != 0:
                snowman.append(a[i])
                a[i] = 0
            i += 1
        else:
            if a[i] != snowman[len(snowman) - 1] and a[i] != 0:
                if len(snowman) < 3:
                    snowman.append(a[i])
                    a[i] = 0
                if len(snowman) == 3:
                    snowman.sort()
                    print(snowman)
                    snowman.clear()
                    i -= 1
                    f += 1
            i += 1
print(f)
