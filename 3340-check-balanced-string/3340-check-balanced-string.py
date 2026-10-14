class Solution:
    def isBalanced(self, num: str) -> bool:
        even,odd=0,0
        for i in range(len(num)):
            if i%2==0:
                even+=int(num[i])
            else:
                odd+=int(num[i])
        return even==odd