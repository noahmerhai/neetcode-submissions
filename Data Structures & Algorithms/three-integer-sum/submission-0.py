class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range (len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0
            beginPos = i + 1
            endPos = len(nums) - 1
            while beginPos < endPos:
                cur = nums[beginPos] + nums[endPos] + nums[i]
                if  cur == target:
                    res.add(tuple(sorted([nums[beginPos] , nums[endPos] , nums[i]])))
                    beginPos += 1
                    endPos -= 1
                elif cur > target:
                    endPos -= 1
                elif cur < target:
                    beginPos += 1
        return [list(x) for x in res]