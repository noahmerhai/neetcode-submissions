from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums).most_common(k)
        lst = []
        for i in range(k):
            lst.append(cnt[i][0])
        
        return lst
        