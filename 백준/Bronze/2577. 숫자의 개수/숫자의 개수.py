total = 1
nums = [0] * 10
for _ in range(3):
    total *= int(input())
for t in str(total):
    nums[int(t)] += 1
print(*nums, sep='\n')