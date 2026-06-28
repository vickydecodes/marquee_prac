nums = [1,2,4,3]

sorted = False

for i in range(1, len(nums)):
    if nums[i - 1] < nums[i]:
        sorted = True
    else:
        sorted = False
        break

print(sorted)

if sorted:
    print('Array is sorted')
else: 
    print('Array not sorted')