import sys
input = sys.stdin.readline
alp = ['ABC', 'DEF', 'GHI',
      'JKL', 'MNO', 'PQRS',
      'TUV', 'WXYZ']
dict_alp = {}
for i, unit in enumerate(alp):
    for w in unit:
        dict_alp[w] = i + 3
        
word = input().strip()
total = 0
for w in word:
    total += dict_alp[w]
print(total)