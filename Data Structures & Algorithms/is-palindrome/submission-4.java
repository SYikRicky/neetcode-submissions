class Solution {
    public boolean isPalindrome(String s) {
        String s1 = s.toLowerCase().replaceAll("[^a-z0-9]", "");
        char[] s_array = s1.toCharArray();
        int l = 0;
        int r = s_array.length - 1;
        while (l < r) {
            if (s_array[l] != s_array[r]) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}
