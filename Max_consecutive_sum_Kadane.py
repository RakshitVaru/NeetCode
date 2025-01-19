class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        curr=0

        for i in nums:
            curr=max(curr,0)+i
            maxsum=max(maxsum, curr)
        return maxsum