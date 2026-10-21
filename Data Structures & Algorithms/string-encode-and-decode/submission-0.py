class Solution:

    def encode(self, strs: List[str]) -> str:
        rtStr = ""
        for word in strs:
            for c in word:
                rtStr = rtStr + "".join(str(ord(c)))
                rtStr = rtStr + "".join("l")
                
            rtStr = rtStr + "".join("n")
        
        return rtStr
    def decode(self, s: str) -> List[str]:
        rtlst = []
        word = ""
        let = ""
        for c in s:
            if c == "l":
                word = word + "".join(chr(int(let)))
                let = ""
            elif c == "n":
                rtlst.append(word)
                print(rtlst)
                word = ""
            else:
                let = let + "".join(c)
                
                
                
        return rtlst