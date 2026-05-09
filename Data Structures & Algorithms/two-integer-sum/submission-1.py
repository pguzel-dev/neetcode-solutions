class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            #  What number would I need with nums[i] to reach the target?
            complement = target - nums[i]
        
            # If I have already seen the number needed to make the target,
            # return its index and my current index.
            if complement in seen:
                return[seen[complement], i]

            # seen stores number -> index so when we are on another number
            # we can see if this one can be used as complement to the new number
            seen[nums[i]] = i