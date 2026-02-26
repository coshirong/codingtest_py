n, x = map(int, input().split())
num_arr = list(map(int, input().split()))
for i in range(n):
    if (num_arr[i] < x):
        print(num_arr[i], end=" ")