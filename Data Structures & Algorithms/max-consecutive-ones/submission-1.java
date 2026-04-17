class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxOnes = 0;
        int ones = 0;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] == 1) {
                ones++;
            }
            else if (nums[i] != 1){
                ones = 0;
            }
            if (ones > maxOnes){
                maxOnes = ones;
            }
        }
        return maxOnes;
    }

}