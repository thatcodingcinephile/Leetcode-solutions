class Solution(object):
    def bitwiseComplement(self, n):
        m=(1<<n.bit_length())-1
        return n^m if n!=0 else 1