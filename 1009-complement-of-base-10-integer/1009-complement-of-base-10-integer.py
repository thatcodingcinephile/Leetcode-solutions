class Solution(object):
    def bitwiseComplement(self, n):
        return int("".join("0" if i=="1" else "1" for i in str(bin(n).replace("0b",""))),2)
