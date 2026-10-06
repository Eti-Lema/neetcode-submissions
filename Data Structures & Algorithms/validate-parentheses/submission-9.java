class Solution {
    public boolean isValid(String s) {
        Stack<Character> opened = new Stack<>();

        for (char curr : s.toCharArray()) {
            if (curr == '(' || curr == '[' || curr == '{') {
                opened.push(curr);
            } else {
                if (opened.empty()) {
                    return false;
                }

                if (curr == ')' && opened.peek() != '(') {
                    return false;
                }

                if (curr == ']' && opened.peek() != '[') {
                    return false;
                }

                if (curr == '}' && opened.peek() != '{') {
                    return false;
                }

                opened.pop();
            }
        }

        return opened.empty();
    }
}