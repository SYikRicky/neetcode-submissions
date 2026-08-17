class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        if (s.length === 0) return true
        let modifiedString = s.split("").filter(i => /[a-zA-Z0-9]/.test(i)).join("").toLowerCase()
        console.log(modifiedString)
        let left = 0;
        let right = modifiedString.length - 1;
        while (left < right) {
            if (modifiedString[left] != modifiedString[right]) return false;
            left++;
            right--;
        }
        return true
    }
}
