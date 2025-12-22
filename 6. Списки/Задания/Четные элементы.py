nums = list(map(int, input().split()))
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        print(nums[i], end=' ')
