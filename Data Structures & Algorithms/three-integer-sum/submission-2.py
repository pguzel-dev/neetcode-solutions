class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set() 
        nums.sort()
    
        def two_sum(start, target):
            valid = set()
            
            for i in range(start, len(nums)):
                
                diff = target - nums[i] 
                if diff in valid:
                    pair = (nums[start - 1], nums[i], diff)  # already sorted
                    res.add(pair)
                
                valid.add(nums[i])
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicate i
                continue
            
            two_sum(i + 1, -nums[i])

        return [list(t) for t in res]