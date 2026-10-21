from collections import Counter 

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ncounter = Counter(nums)
        
        if len(nums) >0  and ncounter.most_common(1)[0][1] > 1:
           return True
        else:
            return False
