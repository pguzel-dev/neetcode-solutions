class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = set() # to prevent unintended duplicates
        nums.sort()

        # two sum with nums[i] being the target
        for i in range(len(nums)):
            # prevent same numbers from popping up again
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            seen = set()
            
            # nums[i] + nums[j] + nums[k] = 0
            # nums[j] + nums[k] = -nums[i]
            target = -nums[i]

            # start by skipping the prev since we already handled those
            for j in range(i + 1, len(nums)):
                # nums[j] + complement = target
                # complement = target + nums[j]
                complement = target - nums[j]

                if complement in seen:
                    solutions.add((nums[i], complement, nums[j]))
                
                seen.add(nums[j])

        return [list(triplet) for triplet in solutions]