import sys
input = sys.stdin.readline
a, b = input().split()
max_val = a[::-1] if int(a[::-1]) > int(b[::-1]) else b[::-1]
print(max_val)