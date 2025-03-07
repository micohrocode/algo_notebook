# Leetcode 268
test = [3,0,1]

def missingNumber(nums):
        # get numbers in order
        nums.sort()

        # check that the first number is correct
        if nums[0]!=0:
            return 0
        
        for i in range(1,len(nums)):
            # check for numbers overall order
            if nums[i] > nums[i-1]+1:
                return nums[i-1]+1
        
        # if all are in order the missing number is the last one
        return len(nums)

missingNumber(test)