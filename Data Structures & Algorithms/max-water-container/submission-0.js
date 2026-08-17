class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        if (heights.length < 1) return 0;
        let l = 0;
        let r = heights.length - 1;
        let res = 0;
        let flag = 0;
        while (l < r) {
            let area = (r - l) * (Math.min(heights[l], heights[r]));
            if (area > res) {
                res = area;
            }
            heights[l] < heights[r] ? l++ : r--;
        }
        return res;
    }
}
