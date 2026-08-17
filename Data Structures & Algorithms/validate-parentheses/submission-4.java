class Solution {
    public boolean isValid(String s) {
        if (s.isEmpty()) return true;
        Stack<Character> check = new Stack<>();
        for (char p : s.toCharArray()) {
            if (!check.empty())
            if (p == '}') { 
                if (check.peek() != '{') return false;
                check.pop();
            } else if (p == ']') {
                if (check.peek() != '[') return false;
                check.pop();
            } else if (p == ')') {
                if (check.peek() != '(') return false;
                check.pop();
            } else {
                check.push(p);
            }
        }
        if (!check.empty()) return false;
        return true;
    }
}
