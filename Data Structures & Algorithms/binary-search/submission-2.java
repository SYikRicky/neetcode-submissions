class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        System.out.println(right);
        while (left <= right) {
            int mid = (int)Math.floor((right + left) / 2);
            System.out.println(mid);
            if (nums[mid] < target) {
                left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
}
