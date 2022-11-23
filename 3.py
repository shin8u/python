import regex as re
f = open('input.txt', 'r', encoding="utf-8")
n = int(f.readline())
answer = []
for i in range(0, n):
    answer.append(0)
k = 0
l = 0
maximum = 0
for ab in f:
    a = []
    a = re.findall(r'\d+', ab)
    b = list(map(int, a))
    i = 0
    S = 0
    for i in b:
        if b[0] >= 40 and b[1] >= 40 and b[2] >= 40:
            S += i
    if S > 0:
        k += 1
    if answer[n-1] < S:
        answer[n-1] = S
    if S > maximum:
        maximum = S
        l = 0
    if S == maximum:
        l += 1
    answer.sort(reverse=True)
f.close()
if k < n or k == n:
    print(0)
else:
    if l > n:
        print(1)
    else:
        print(answer[n-1])
