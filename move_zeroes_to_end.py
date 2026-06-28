class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # assuming we allocate the index at 0 for left and further more we calculate with the nums[i] 
        left = 0
        for i in range(len(nums)):
            print(left)
            if nums[i] != 0:
                nums[i], nums[left] = nums[left], nums[i]
                print(nums[i], nums[left])
                left += 1
        return nums
                    
                    
solution = Solution()

print(solution.moveZeroes([0,1,0,3,12]))
                    
                    