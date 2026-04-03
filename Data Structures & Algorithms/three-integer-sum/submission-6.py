class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i, target in enumerate(nums):
            if i > 0 and target == nums[i - 1]:
                continue

            left, right = i+1, len(nums)-1
            while left < right:
                threeSum = target + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    results.append([target, nums[left], nums[right]])
                    left += 1

                    while left < right and nums[left] == nums [left - 1]:
                        left += 1
        
        return results