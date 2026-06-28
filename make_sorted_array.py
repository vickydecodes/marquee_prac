nums = [5,1,3,4,2]

for i in range(len(nums)):
    for j in range(len(nums) - 1):
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            
print(nums)
matrix = [[1,2,3], [4,5,6], [7,8,9]]
#### 0 0, 0 1, 0 2, 1 0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        print('iterating variables',i,j)
        print(matrix[i][j])
        