n = int(input())
for _ in range(n):
    scores = input()
    cnt = 0
    total = 0
    for s in scores:
        if (s=='O'):
            cnt += 1
            total += cnt
        else: 
            cnt = 0
    print(total)