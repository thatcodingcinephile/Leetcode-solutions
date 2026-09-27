//Another Code by Class XII Rookie
import java.util.*;
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int ar[]=new int[2];
        for(int i=0; i<nums.length; i++){
            for(int j=i; j<nums.length;j++){
                if(nums[i]+nums[j]==target){
                   if(i!=j){
                   ar[0]=i;
                   ar[1]=j;
                   break;
                   }
                   else{ 
                   continue;
                   
                   }
                }
            }
        }
        return ar;
    }
    public static void main(){
        Scanner in=new Scanner(System.in);
        Solution ob=new Solution();
        System.out.println("Enter Array Size");
        int len=in.nextInt();
        int nums[]=new int[len];
        for(int i=0;i<len; i++){
            nums[i]=in.nextInt();
        }
        System.out.println("Enter Target :");
        int target=in.nextInt();
        System.out.println("Output :"+ob.twoSum(nums , target));
    }
}