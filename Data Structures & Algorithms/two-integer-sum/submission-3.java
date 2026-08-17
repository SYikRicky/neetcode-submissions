class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int secondNum = target - nums[i];
            System.out.println(map);
            if (map.containsKey(secondNum)) {
                return new int[]{map.get(secondNum), i};
            }
            map.put(nums[i], i);
        }
        return new int[0];
    }
}
