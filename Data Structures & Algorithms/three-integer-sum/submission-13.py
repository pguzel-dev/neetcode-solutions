class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        # helper function: finds all triplets using a fixed number
        def two_sum(start: int, target: int, fixed: int) -> Set[Tuple[int, int, int]]:
            valid = set()          # seen numbers
            local_res = set()      # unique triplets for this call

            for i in range(start, len(nums)):
                diff = target - nums[i]

                if diff in valid:
                    # build triplet with fixed element
                    local_res.add((fixed, nums[i], diff))

                valid.add(nums[i])

            return local_res

        res = set()

        for i in range(len(nums)):
            # skip duplicate fixed elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            fixed = nums[i]

            # nums[j] + nums[k] = -fixed
            res.update(two_sum(i + 1, -fixed, fixed))

        return [list(t) for t in res]