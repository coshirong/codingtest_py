import sys
input = sys.stdin.readline
word = input().strip()
total = 0
alp = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
for w in word:
    for i, sett in enumerate(alp):
        if w in sett:
            total += i + 3
            break
print(total)