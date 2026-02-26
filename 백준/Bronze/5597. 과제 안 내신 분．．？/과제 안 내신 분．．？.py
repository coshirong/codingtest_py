nums = set()
for _ in range(28):
    nums.add(int(input()))
for i in range(1, 31):
    if i not in nums:
        print(i)