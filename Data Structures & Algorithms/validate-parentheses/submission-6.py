class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) < 2:
            return False
        stack = []
        first_char = s[0]
        
        if first_char not in {'(', '{', '['}:
            return False
        
        stack.append(first_char)

        for i in range(1, len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif not stack or (s[i] == ')' and stack[-1] != '(') or ((s[i] == '}' and stack[-1] != '{')) or ((s[i] == ']' and stack[-1] != '[')):
                return False
            else:
                stack.pop()
        return len(stack) == 0
            
            