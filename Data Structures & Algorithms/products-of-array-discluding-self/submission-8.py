class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        mult = 1
        
        for j in range(len(nums)):
            for i in range(len(nums)):
                if i != j:
                     mult *= nums[i]
            
            output.append(mult)
            mult = 1
            
        return output 
        