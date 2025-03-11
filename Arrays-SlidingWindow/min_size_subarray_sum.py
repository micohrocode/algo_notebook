# leetcode 209
test = [2,3,1,2,4,3]
target = 7

def minSubArrayLen(target, nums):
        # left pointer
        l = 0
        # check total
        total = 0
        # result to compare to each time
        res = float('inf')

        for r in range(len(nums)):
            # add the new number to the total
            total += nums[r]

            # while the total meets the requirements
            while total >= target:
                # check if the length is smaller
                res = min(res, r-l+1)

                # make the length smaller and check
                # while condition again
                total -= nums[l]
                l+=1
        
        if res == float('inf'):
            return 0
        else:
            return res
        
minSubArrayLen(target,test)