class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        for (let i = 0; i < matrix.length; i++) {
            let l = 0;
            let r = matrix[i].length - 1;
            while (l <= r) {
                let m = l + Math.floor((r - l) / 2);
                if (matrix[i][m] < target) {
                    l = m + 1;
                } else if (matrix[i][m] > target) {
                    r = m - 1;
                } else {
                    return true;
                }
            }
        }
        return false;
    }
}
