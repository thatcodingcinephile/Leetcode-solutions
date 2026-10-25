class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int("".join("0" if i=="1" else "1" for i in str(bin(n).replace("0b",""))),2)