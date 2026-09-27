import java.util.*;
class Solution
{
		 String intToRoman(int n)
		{
              int   x=n;
              int  v[]={3000,2000,1000,900,800,700,600,500,400,300,200,100,90,80,70,60,50,40,30,20,10,9,8,7,6,5,4,3,2,1};
              
             String m[]={"MMM", "MM", "M", "CM","DCCC","DCC","DC","D","CD","CCC","CC","C","XC","LXXX","LXX","LX","L","XL","XXX","XX","X","IX","VIII","VII","VI","V","IV","III","II","I"};
            String nm="";
            for(int i=0; i<v.length; i++)
            {
                if(x>=v[i])
                { 
                    nm+=m[i];
                    x-=v[i];
                    }
            }
            return nm;
	}
	public static void main(String args[])
	{
	    Solution ob=new Solution();
	    Scanner in=new Scanner(System.in);
	    System.out.println("Enter Number :");
	    int num=in.nextInt();
	    System.out.println("Roman Equivalent :" +ob.intToRoman(num));
	    }
}