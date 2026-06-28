nums = [4,3,2,7,8,2,3,1]

duplicates = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j] and nums[i] not in duplicates:
            duplicates.append(nums[i])
            
print(duplicates)


arr = [4, 3, 2, 7, 8, 2, 3, 1]

seen = set()
duplicates = []

for num in arr:
    if num in seen:
        duplicates.append(num)
    else:
        seen.add(num)

print(duplicates)