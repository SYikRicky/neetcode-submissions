class Solution {
    /**
     * @param {numbers[]} numbers
     * @param {numbers} target
     * @return {numbers[]}
     */
    twoSum(numbers, target) {
        let l = 0;
        let r = numbers.length - 1;
        while (numbers[l] + numbers[r] != target) {
            if (numbers[l] + numbers[r] > target) {
                r--;
            } else {
                l++;
            }
        }
        console.log([numbers[l],numbers[r]])
        return [l+1,r+1]
    }
}
