class Solution:
    def addBinary(self, a: str, b: str) -> str:
        temp1,temp2=int(a),int(b)
        def BintoDec(x: str):
            dec,c,temp=0,0,0
            tempbin=int(x)
            while tempbin>0:
                temp=tempbin%10
                dec+=(temp*pow(2,c))
                c+=1
                tempbin//=10
            return int(dec)
        sum=BintoDec(temp1)+BintoDec(temp2)
        st=""
        c=0
        while sum>0:
           c=sum%2
           st+=str(c)
           sum//=2
        if(a==b=="0"):
             return "0"
        else: 
             return st[::-1]