class Solution {
    public boolean isValid(String s) {
        if (s.isEmpty()) return true;
        Stack<Character> check = new Stack<>();
        for (char p : s.toCharArray()) {
            if (p == '}') { 
                if (check.empty() || check.peek() != '{') return false;
                check.pop();
            } else if (p == ']') {
                if (check.empty() || check.peek() != '[') return false;
                check.pop();
            } else if (p == ')') {
                if (check.empty() || check.peek() != '(' ) return false;
                check.pop();
            } else {
                check.push(p);
            }
        }
        return check.isEmpty();
    }
}
