class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        if (tokens.length === 0) return 0;
        const stack = [];
        for (let i = tokens.length - 1; i >= 0; i--) {
            stack.push(tokens[i])
        }
        let a = Number(stack.pop());
        let b = Number(stack.pop());
        let optors = stack.pop();
        while (true) {
            // a optors b
            console.log(`a: ${a}, b: ${b}, optors: ${optors}`)
            if (optors === "+") {
                a = a + b;
            } else if (optors === "-") {
                a = a - b
            } else if (optors === "*") {
                a = a * b
            } else if (optors === "/") {
                a = a / b
            }
            b = Number(stack.pop());
            optors = stack.pop();
            if (!b || !optors) break;
        }
        return a;
    }
}
