from collections import *
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for i in range(len(strs)):
            

            words["".join(sorted(strs[i]))].append(strs[i])
            
        return list(words.values())