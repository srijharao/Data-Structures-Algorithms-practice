class Solution {
    public boolean isValid(String s) {

        if(s.length() <= 1) return false;

        Stack<Character> stack = new Stack<>();

        for(int i=0; i< s.length(); i++){
            if(s.charAt(i) == ')'){
                if(stack.isEmpty() || stack.pop() != '(') return false;
            } else if(s.charAt(i) == ']'){
                if(stack.isEmpty() || stack.pop() != '[') return false;
            } else if(s.charAt(i) == '}'){
                if(stack.isEmpty() || stack.pop() != '{') return false;
            } else{
                stack.push(s.charAt(i));
            }
        }
        if(stack.isEmpty()){
            return true;
        }
        return false;
    }
}
