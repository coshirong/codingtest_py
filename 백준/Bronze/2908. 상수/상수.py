a, b = map(str, input().split())
res = a[::-1] if a[::-1] > b[::-1] else b[::-1]
print(res)