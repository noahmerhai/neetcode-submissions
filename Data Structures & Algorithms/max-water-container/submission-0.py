class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights)-1
        ret = 0
        while L < R:
            if min(heights[R],heights[L]) * (R-L) > ret:
                ret = min(heights[R],heights[L]) * (R-L)
            if heights[L] < heights[R]:
                L+=1
            else: 
                R-=1
        return ret
            