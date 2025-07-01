class Solution {
public:
    int robLinear(vector<int>& nums, int start, int end) {
        int prev = 0, curr = 0;
        for (int i = start; i <= end; ++i) {
            int temp = max(curr, prev + nums[i]);
            prev = curr;
            curr = temp;
        }
        return curr;
    }

    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        if (n == 2) return max(nums[0], nums[1]);

        return max(robLinear(nums, 0, n - 2), robLinear(nums, 1, n - 1));
    }
};
