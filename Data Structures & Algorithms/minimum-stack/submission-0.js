class MinStack {
    constructor() {
        this.stack = [];
        this.minValueStack = [];
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.stack.push(val);
        if (this.minValueStack.length === 0) {
            this.minValueStack.push(val);
        } else {
            let prevMin = this.minValueStack[this.minValueStack.length - 1]
            if (val < prevMin) {
                this.minValueStack.push(val);
            } else {
                this.minValueStack.push(prevMin);
            }
        }
    }

    /**
     * @return {void}
     */
    pop() {
        this.stack.pop();
        this.minValueStack.pop();
    }

    /**
     * @return {number}
     */
    top() {
        return this.stack[this.stack.length - 1];
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.minValueStack[this.minValueStack.length - 1];
    }
}
