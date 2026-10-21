class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        beginPos = 0
        
        endPos = len(numbers) -1
        while beginPos < len(numbers) -1:
            cur = numbers[beginPos] + numbers[endPos]
            if  cur == target:
                return [beginPos+1 ,endPos+1]
            elif cur > target:
                endPos -=1
            elif cur < target:
                beginPos +=1
                