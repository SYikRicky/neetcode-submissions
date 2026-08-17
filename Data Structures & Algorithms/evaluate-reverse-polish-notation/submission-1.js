class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        if (tokens.length === 0) return 0;
        const stack = [];
        for (let i = 0; i < tokens.length; i++) {
            if (isNaN(Number(tokens[i]))) {
                let b = stack.pop();
                let a = stack.pop();
                console.log(`a :${a}, b :${b}`)
                if (tokens[i] === "+") {
                    stack.push(a + b)
                } else if (tokens[i] === "-") {
                    stack.push(a - b);
                } else if (tokens[i] === "*") {
                    stack.push(a * b);
                } else if (tokens[i] === "/") {
                    stack.push(parseInt((a / b), 10));
                }
            } else {
                stack.push(Number(tokens[i]));
            }
        } 
        return stack.pop();
    }
}
