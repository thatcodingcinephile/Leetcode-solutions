class Solution:
    def validStrings(self, n: int) -> List[str]:
        l=[]
        for i in range((2**n)):
            b=f"{i:0{n}b}"
            if "00" not in b:
                l.append(b)
        return l