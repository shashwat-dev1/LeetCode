class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0; // next position for non-val
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val) {
                nums[k++] = nums[i];
            }
        }
        return k;
    }
};