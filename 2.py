n = int(input())
snowman = []
all_snowman = {}
a = list(map(int, input().split()))
a.sort()
count = 0
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
                    i -= 1
                    count += 1
                    all_snowman[count] = snowman
                    snowman = []
            i += 1
print(count)
for i in range(1, count + 1):
    answer = map(str, all_snowman[i])
    print(' '.join(answer))
