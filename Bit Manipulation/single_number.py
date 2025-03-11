# leetcode 136
test = [2,2,1]

def singleNumber(self, nums):
        xor = 0
        for i in nums:
            # any duplicates will result in 0,
            # so the only remaining thing will be the 
            # number without a duplicate
            xor^=i
        return xor