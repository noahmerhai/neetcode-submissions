class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sl = ''.join(sorted(s))
        tl =  ''.join(sorted(t))

        if sl == tl:
            return True
        else:
            return False