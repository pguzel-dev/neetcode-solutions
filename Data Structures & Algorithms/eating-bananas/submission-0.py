class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possibleHour(rate):
            total_h = 0
            for amount in piles:
                total_h += math.ceil(amount / rate)
            return total_h

        # upper bound would be the most bananas in the array
        low_r, up_r = 1, max(piles)

        while low_r <= up_r:
            sug_r = low_r + ((up_r - low_r) // 2)
            time = possibleHour(sug_r)

            # not possible, we need to increase
            if time > h:
                low_r = sug_r + 1
                
            # possible, we can decrease it
            elif time <= h:
                up_r = sug_r - 1
            
        return low_r