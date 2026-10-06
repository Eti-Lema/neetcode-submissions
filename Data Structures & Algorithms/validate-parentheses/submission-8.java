class Solution {
    public boolean isValid(String s) {
        Stack<Character> opened = new Stack<>();

        char first = s.charAt(0);
        if (first == '[' || first == '(' || first == '{'){
                opened.push(first);
        } else {
            return false;
        }
        
        for(int i = 1; i < s.length(); i++) {
            char curr = s.charAt(i);
            if (curr == '[' || curr == '(' || curr == '{'){
                opened.push(curr);
            } else if (opened.empty()){
                return false;
            } else if (curr == '}' && opened.peek() != '{'){
                return false;
            } else if (curr == ')' && opened.peek() != '('){
                return false;
            } else if (curr == ']' && opened.peek() != '['){
                return false;
            } else {
                opened.pop();
            }
        }

        return opened.empty();
    }
}
