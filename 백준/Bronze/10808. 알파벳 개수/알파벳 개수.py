word = input()
conts = [0] * 26
for w in word:
    w = ord(w) - ord('a')
    conts[w]+=1
print(*conts)