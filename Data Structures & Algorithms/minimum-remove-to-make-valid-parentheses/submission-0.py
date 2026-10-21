from collections import deque
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        word = []
        openCnt = 0
        for c in s:
            if c == '(':
                openCnt +=1
                word.append(c)
            elif c == ')' and openCnt != 0:
                word.append(c)
                openCnt -=1
            elif c.isalnum():
                word.append(c)
        if openCnt != 0:
            word = "".join(word)[::-1].replace('(','',openCnt)[::-1]
        return "".join(word)
        