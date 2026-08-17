class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        let res = new Array(temperatures.length).fill(0); 
        let stack = []; // [[temp, index]...]
        for (let i = 0; i < temperatures.length; i++) {
            if (i === 0) {
                stack.push([temperatures[i], i]);
                continue;
            }
            
            while (stack.length > 0) {
                let prevTemp = stack[stack.length - 1][0];
                let prevIndex = stack[stack.length - 1][1];
                if (temperatures[i] > prevTemp) {
                    res[prevIndex] = i - prevIndex;
                    stack.pop();
                } else {
                    break;
                }
            }
            stack.push([temperatures[i], i]);
        }
        return res;
    }
}
