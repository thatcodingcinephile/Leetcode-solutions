class Solution:
    def hammingWeight(self, n: int) -> int:
        st=bin(n).replace("0b","")
        count=0
        for i in st:
            if i=="1":
                count+=1
        return count
