class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = -1
        i = 0
        while(i < len(nums) // 2):
            temp_sum = nums[i] + nums[len(nums) - i - 1]
            if(temp_sum > max_sum):
                max_sum = temp_sum
            i += 1
        return max_sum