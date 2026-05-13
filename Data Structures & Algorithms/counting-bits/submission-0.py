class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def bit_counter(num):
            res = 0
            while num:
                num = num & (num - 1)
                res += 1
            return res
        
        result = []
        for num in range(n+1):
            result.append(bit_counter(num))

        return result