word= input()
conts = [-1] * 26
for i, ch in enumerate(word):
    if conts[ord(ch) - ord('a')] == -1:
        conts[ord(ch) - ord('a')] = i
print(*conts)