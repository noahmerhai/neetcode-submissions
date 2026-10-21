class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        mult = 1
        
        for j in range(len(nums)):
            for i in range(1,len(nums)):
                if i != j:
                     mult *= nums[i]
            
            output.append(mult)
            mult = nums[0]
            
        return output 
        