n, x = map(int, input().split())
num_arr = list(map(int, input().split()))
for num in num_arr:
    if (num < x):
        print(num, end=" ")