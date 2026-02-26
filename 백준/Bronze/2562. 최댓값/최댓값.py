nums = []
for _ in range(9):
    nums.append(int(input()))    
big = nums[0]
for n in nums:
    if (n > big):
        big = n
print(big)
print(nums.index(big) + 1)