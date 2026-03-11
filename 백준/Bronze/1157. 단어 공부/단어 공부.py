import sys
input = sys.stdin.readline

word = input().strip().upper()
count = {}
for w in word:
    count[w] = count.get(w, 0) + 1

res = max(count.values())
winners = []
for k, v in count.items():
    if v == res:
        winners.append(k)

if (len(winners) > 1):
    print('?')
else:
    print(winners[0])