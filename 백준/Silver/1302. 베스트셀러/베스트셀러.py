import sys
input = sys.stdin.readline

# 입력
cnt = int(input())
name = []
for _ in range(cnt):
    name.append(input().strip())
name.sort()

# 제목:개수 짝 만들기
books_cnt = {}
for n in name:
    books_cnt[n] = books_cnt.get(n, 0) + 1

# 개수가 최대인
max_val = max(books_cnt.values())
for k, v in books_cnt.items():
    if v == max_val:
        print(k)
        break