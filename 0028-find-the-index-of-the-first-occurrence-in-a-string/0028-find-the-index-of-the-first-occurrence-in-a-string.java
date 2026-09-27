import java.util.*;
public class Solution {
    public int strStr(String haystack, String needle) {
        if(haystack.indexOf(needle)>=0){
            return haystack.indexOf(needle);
        }
        else return -1;
        }
    public static void main(){
        Scanner in =new Scanner(System.in);
        Solution ob=new Solution();
        System.out.println("Enter haystack :");
        String haystack= in.next();
        System.out.println("Enter Needle :");
        String needle= in.next();
        if(haystack.length()<1 || needle.length()>10){
            System.out.println("Invalid Input");
            return;
        }
        else if(haystack.equals(haystack.toLowerCase())!=true|| needle.equals(needle.toLowerCase())!=true){
            System.out.println("Input should be in lowercase only :)");
            return;
        }
       System.out.println("Index :"+ob.strStr(haystack , needle));
    }
    }
