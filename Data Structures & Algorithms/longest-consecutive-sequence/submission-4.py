class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cnt = 0
        nums = set(nums)
        for num in nums:
            if num -1 not in nums:
                leng = 1
                while (num + leng) in nums:
                    leng+=1
                cnt = max(leng, cnt)
            
        return cnt
            
