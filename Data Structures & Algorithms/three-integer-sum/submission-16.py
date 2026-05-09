class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        # Finds all pairs after `start` that sum to `target`,
        # then combines each pair with `fixed`.
        def two_sum(start: int, fixed: int, target: int) -> Set[Tuple[int, int, int]]:
            seen = set()
            triplets = set()

            for i in range(start, len(nums)):
                complement = target - nums[i]

                if complement in seen:
                    triplet = (fixed, nums[i], complement)
                    triplets.add(tuple(sorted(triplet)))

                seen.add(nums[i])

            return triplets

        for i in range(len(nums)):
            # Skip duplicate fixed values to avoid repeated work.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            fixed = nums[i]
            target = -fixed

            # Need nums[j] + nums[k] = -nums[i].
            result.update(two_sum(i + 1, fixed, target))

        return [list(triplet) for triplet in result]