import sys
input = sys.stdin.readline
word = input()
total = 0
alp = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
for w in word:
    for i in range(len(alp)):
        if w in alp[i]:
            total += (i+3)
print(total)