class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stack = [];
        if (s.length < 2) return false;

        for (let i = 0; i < s.length; i++) {
            if (s[i] === "(" || s[i] === "[" || s[i] === "{") {
                stack.push(s[i]);
            } else {
                if (s[i] === ")" && stack.pop() !== "(") return false;
                if (s[i] === "]" && stack.pop() !== "[") return false;
                if (s[i] === "}" && stack.pop() !== "{") return false;
            }
        }
        if (stack.length !== 0) return false;
        return true;
    }
}
