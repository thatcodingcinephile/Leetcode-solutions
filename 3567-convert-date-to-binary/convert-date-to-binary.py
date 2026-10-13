class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date=list(map(int,date.split("-")))
        date=list(map(bin,date))
        l=[]
        for i in date:
            l.append(i.replace("0b",""))
        return "-".join(l)