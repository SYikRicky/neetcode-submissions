class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        if (s.length === 0) return true
        let modifiedString = s.split("").filter(i => /[a-zA-Z]/.test(i)).join("").toLowerCase()
        console.log(modifiedString)
        let left = 0;
        let right = modifiedString.length - 1;
        while (left != right) {
            let charOne = modifiedString[left];
            let charTwo = modifiedString[right];
            if (charOne != charTwo) return false;
            left++;
            right--;
        }
        return true
    }
}
