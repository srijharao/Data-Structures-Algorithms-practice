class Solution {
    public boolean isPalindrome(String s) {

        String lower = s.toLowerCase();
        int i = 0;
        int j = lower.length()-1;
        System.out.println(lower);
        
        while(i<j){
            if (!isValid(lower.charAt(i))){
                i++;
            }
            else if(!isValid(lower.charAt(j))){
                j--;
            }
            else if(lower.charAt(i) != (lower.charAt(j))){
                    return false;
            }
            else{
                i++;
                j--;
            }
        }
        return true;
    }

    Boolean isValid(char c){
        if(Character.isDigit(c) || Character.isLetter(c)){
            return true;
        }
        return false;
    }
}
