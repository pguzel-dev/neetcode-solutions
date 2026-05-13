class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def simple_rob(loot: List[int]) -> int:
            loot.append(0)
    
            for index in range(len(loot) - 3, -1, -1):
                loot[index] = max(loot[index] + loot[index + 2], loot[index + 1])

            return loot[0]
        
        return max(simple_rob(nums[:-1]), simple_rob(nums[1:]))