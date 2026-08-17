class Solution {
    public boolean isValid(String s) {
        if (s.isEmpty()) return true;
        Stack<Character> check = new Stack<>();
        for (char p : s.toCharArray()) {
            if (p == '}') { 
                if (check.pop() != '{') return false;
            } else if (p == ']') {
                if (check.pop() != '[') return false;
            } else if (p == ')') {
                if (check.pop() != '(') return false;
            } else {
                check.push(p);
            }
        }
        return true;
    }
}
